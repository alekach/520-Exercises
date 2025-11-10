import subprocess
import re
import os
import csv
from tabulate import tabulate

PROBLEMS = [f'HumanEval_{i}' for i in range(10)]
LLMS = ['grok', 'chatgpt']
FULL_CODE_BASE_DIR = 'full_generated_code'  # Use the new full code folder
TEST_DIR = 'tests'                          # Directory where test files are
COVERAGE_REPORT_DIR = 'coverage_reports/baseline'  # Where to save HTML reports
SAMPLES = range(1, 6)                       # Samples 1 to 5

# Ensure directories exist
os.makedirs(COVERAGE_REPORT_DIR, exist_ok=True)

# Project root for PYTHONPATH
PROJECT_ROOT = os.getcwd()  # Assumes you run this from the project root

# Function to run pytest with coverage and parse output
def run_coverage(problem_id, llm, sample_num):
    code_dir = os.path.join(FULL_CODE_BASE_DIR, llm, problem_id)
    module_name = f"{FULL_CODE_BASE_DIR}.{llm}.{problem_id}.sample{sample_num}"  # For --cov= (without .py)
    
    test_file = os.path.join(TEST_DIR, f"test_{problem_id}_{llm}_sample{sample_num}.py")
    
    if not os.path.exists(code_dir) or not os.path.exists(test_file):
        print(f"Skipping {problem_id} ({llm} sample{sample_num}): Missing code or test file.")
        return None  # Skip if files missing
    
    # Command to run pytest with coverage
    cmd = [
        'pytest',
        '--cov=' + module_name,
        '--cov-branch',
        '--cov-report=term-missing',
        '--cov-report=html:' + os.path.join(COVERAGE_REPORT_DIR, f"{problem_id}_{llm}_sample{sample_num}_html"),
        '-v',  # Add verbose for more detailed output/tracebacks
        test_file
    ]
    
    # Set environment with PYTHONPATH to include project root
    env = os.environ.copy()
    env['PYTHONPATH'] = PROJECT_ROOT + (os.pathsep + env.get('PYTHONPATH', ''))
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, env=env)
    except subprocess.CalledProcessError as e:
        output = e.output  # Capture output even if error
    
    # Print the full output for debugging (shows errors/tracebacks)
    print(f"\n=== Output for {problem_id} ({llm} sample{sample_num}) ===\n{output}\n=== End Output ===\n")
    
    # Parse number of tests passed/failed
    passed_match = re.search(r'(\d+) passed', output)
    failed_match = re.search(r'(\d+) failed', output)
    total_tests = 0
    passed = int(passed_match.group(1)) if passed_match else 0
    failed = int(failed_match.group(1)) if failed_match else 0
    total_tests = passed + failed
    tests_passed_str = f"{passed}/{total_tests}"
    
    # Parse coverage: Look for TOTAL line
    total_match = re.search(r'TOTAL\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)%', output)
    if total_match:
        stmts = int(total_match.group(1))
        miss = int(total_match.group(2))
        branches = int(total_match.group(3))
        br_miss = int(total_match.group(4))
        line_cover = 100 - (miss / stmts * 100) if stmts > 0 else 0
        branch_cover = 100 - (br_miss / branches * 100) if branches > 0 else 0
    else:
        line_cover = 0
        branch_cover = 0
    
    # Basic note: Customize manually later based on HTML reports
    note = ""
    if branch_cover < 50:
        note = "Low branch coverage due to untested branches/conditions."
    elif line_cover < 70:
        note = "Moderate coverage; some lines untested."
    else:
        note = "Good coverage, but check for edge cases."
    
    return {
        'problem': f"{problem_id} ({llm} sample{sample_num})",
        'tests_passed': tests_passed_str,
        'line_%': f"{line_cover:.1f}%",
        'branch_%': f"{branch_cover:.1f}%",
        'notes': note
    }

# Collect results
results = []
for problem_id in PROBLEMS:
    for llm in LLMS:
        for sample_num in SAMPLES:
            result = run_coverage(problem_id, llm, sample_num)
            if result:
                results.append(result)

# Generate summary table
if results:
    table = [[r['problem'], r['tests_passed'], r['line_%'], r['branch_%'], r['notes']] for r in results]
    
    # Write to CSV with proper quoting
    with open('baseline_coverage.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Problem (LLM Sample)', 'Tests Passed', 'Line Coverage %', 'Branch Coverage %', 'Notes'])
        writer.writerows(table)
    
    print("Table written to baseline_coverage.csv")
else:
    print("No results found. Check file paths and structure.")