import subprocess
import re
import os

SELECTED = [
    {'problem_id': 'HumanEval_0', 'llm': 'chatgpt', 'sample_num': 1},
    {'problem_id': 'HumanEval_4', 'llm': 'grok', 'sample_num': 2}
]
SEED_CODE_BASE_DIR = 'seeded_code'  # Directory with tampered/seeded code files
IMPROVED_TEST_DIR = 'seeded_tests'  # Directory with improved test files

# Project root for PYTHONPATH
PROJECT_ROOT = os.getcwd()

# Function to run improved tests on seeded code and check pass/fail
def run_fault_detection(problem_id, llm, sample_num):
    code_dir = os.path.join(SEED_CODE_BASE_DIR, llm, problem_id)
    module_name = f"{SEED_CODE_BASE_DIR}.{llm}.{problem_id}.sample{sample_num}"  # For import in tests

    test_file = os.path.join(IMPROVED_TEST_DIR, f"test_{problem_id}_{llm}_sample{sample_num}.py")
    
    if not os.path.exists(code_dir) or not os.path.exists(test_file):
        print(f"Skipping {problem_id} ({llm} sample{sample_num}): Missing seeded code or improved test file.")
        return None
    
    # Command to run pytest (no coverage, just test execution)
    cmd = [
        'pytest',
        '-v',  # Verbose for details
        test_file
    ]
    
    # Set environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = PROJECT_ROOT + (os.pathsep + env.get('PYTHONPATH', ''))
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, env=env)
    except subprocess.CalledProcessError as e:
        output = e.output
    
    # Print full output for debugging
    print(f"\n=== Output for {problem_id} ({llm} sample{sample_num}) ===\n{output}\n=== End Output ===\n")
    
    # Parse to check if all tests passed
    passed_match = re.search(r'(\d+) passed', output)
    failed_match = re.search(r'(\d+) failed', output)
    passed = int(passed_match.group(1)) if passed_match else 0
    failed = int(failed_match.group(1)) if failed_match else 0
    total_tests = passed + failed
    
    if total_tests > 0 and failed > 0:
        status = "Failed (bug detected)"
    elif total_tests > 0 and passed == total_tests:
        status = "Passed (no bug detected)"
    else:
        status = "No tests ran or error"
    
    return {
        'problem': f"{problem_id} ({llm} sample{sample_num})",
        'status': status
    }

# Run for selected
results = []
for sel in SELECTED:
    result = run_fault_detection(sel['problem_id'], sel['llm'], sel['sample_num'])
    if result:
        results.append(result)

# Print simple results
for r in results:
    print(f"{r['problem']}: {r['status']}")