import os
import csv
import subprocess
import tempfile
import json  # Added for failure logging
from human_eval.data import read_problems, write_jsonl

def custom_check_correctness(task_id, completion, prompt, test, entry_point, timeout=5.0):
    # Combine prompt (sig + docstring) + completion (body) + test
    full_code = prompt + completion + '\n' + test + f'\ncheck({entry_point})'

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(full_code)
        temp_file_path = temp_file.name

    try:
        # Run the file with timeout
        result = subprocess.run(['python', temp_file_path], capture_output=True, text=True, timeout=timeout)
        if result.returncode == 0:
            return {"passed": True, "result": result.stdout}
        else:
            return {"passed": False, "result": f"failed: {result.stderr or result.stdout}"}
    except subprocess.TimeoutExpired:
        return {"passed": False, "result": "timed out"}
    except Exception as e:
        return {"passed": False, "result": f"failed: {str(e)}"}
    finally:
        os.unlink(temp_file_path)  # Clean up

def custom_evaluate_functional_correctness(samples_jsonl, problem, k, timeout=5.0):
    # Simplified pass@k calculation (since small k, no bootstrap)
    samples = []
    with open(samples_jsonl, 'r') as f:
        for line in f:
            samples.append(eval(line.strip()))

    results = []
    failures = []  # Track failures here
    for idx, sample in enumerate(samples, start=1):  # Start from 1 to match sample1.py, etc.
        result = custom_check_correctness(sample['task_id'], sample['completion'], problem['prompt'], problem['test'], problem['entry_point'], timeout)
        results.append(result)
        if not result['passed']:
            failures.append({
                'sample_id': f'sample{idx}.py',
                'error': result['result']
            })

    # Compute pass@k
    n = len(samples)
    pass_counts = {}
    for val in k:
        pass_counts[val] = sum(1 for r in results[:val] if r['passed']) / val if val <= n else 0.0  # Simple average for small n

    return pass_counts, failures  # Return failures too

if __name__ == '__main__':
    # Config
    MODEL = 'chatgpt' # or 'grok'
    K = 5
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROBLEMS_DIR = os.path.join(SCRIPT_DIR, '..', 'generated_code', MODEL)
    RESULTS_DIR = os.path.join(SCRIPT_DIR, '..', 'results')
    TIMEOUT = 5.0  # Now using subprocess timeout (Windows-friendly)
    PROBLEM_FILE = 'C:/Users/ajlms/OneDrive/Desktop/520/project-1/human-eval/data/HumanEval.jsonl.gz'
    CSV_OUTPUT = os.path.join(RESULTS_DIR, f'pass_k_results_{MODEL}.csv')

    problems = read_problems(PROBLEM_FILE)

    all_results = []

    for task_id in os.listdir(PROBLEMS_DIR):
        samples = []
        problem_dir = os.path.join(PROBLEMS_DIR, task_id)
        if not os.path.isdir(problem_dir):
            continue

        for i in range(1, K + 1):
            sample_file = os.path.join(problem_dir, f'sample{i}.py')
            if os.path.exists(sample_file):
                with open(sample_file, 'r') as f:
                    completion = f.read()
                samples.append({
                    'task_id': task_id.replace('_', '/'),
                    'completion': completion
                })

        if samples:
            jsonl_path = os.path.join(RESULTS_DIR, f'{MODEL}_{task_id}_samples.jsonl')
            write_jsonl(jsonl_path, samples)

            full_task_id = task_id.replace('_', '/')
            if full_task_id in problems:
                problem = problems[full_task_id]
            else:
                print(f"Skipping {task_id}: Not found in problems")
                continue

            try:
                pass_counts, failures = custom_evaluate_functional_correctness(jsonl_path, problem, k=[1, 5], timeout=TIMEOUT)
                print(f"Results for {task_id}: {pass_counts}")

                all_results.append({
                    'model': MODEL,
                    'task_id': task_id,
                    'pass@1': pass_counts.get(1, 0.0),
                    'pass@5': pass_counts.get(5, 0.0)
                })

                # Save failures if any
                if failures:
                    failures_path = os.path.join(RESULTS_DIR, f'{MODEL}_{task_id}_failures.json')
                    with open(failures_path, 'w') as f:
                        json.dump(failures, f, indent=4)
                    print(f"Failures saved for {task_id} to {failures_path}")
            except Exception as e:
                print(f"Error evaluating {task_id}: {e}")
        else:
            print(f"No samples found for {task_id}")

    if all_results:
        with open(CSV_OUTPUT, 'w', newline='') as csvfile:
            fieldnames = ['model', 'task_id', 'pass@1', 'pass@5']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_results)
        print(f"Results saved to {CSV_OUTPUT}")
    else:
        print("No results to save.")