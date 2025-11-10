import subprocess
import re
import os
import csv

SELECTED = [
    {'problem_id': 'HumanEval_0', 'llm': 'chatgpt', 'sample_num': 1},
    {'problem_id': 'HumanEval_4', 'llm': 'grok', 'sample_num': 2}
]
FULL_CODE_BASE_DIR = 'full_generated_code'  # Directory with full code files
IMPROVED_TEST_DIR = 'improved_tests'        # New directory for improved tests
COVERAGE_REPORT_DIR = 'coverage_reports/improved'  # Where to save improved HTML reports

# Ensure directories exist
os.makedirs(IMPROVED_TEST_DIR, exist_ok=True)
os.makedirs(COVERAGE_REPORT_DIR, exist_ok=True)

# Function to run pytest with coverage on improved tests and parse output
def run_improved_coverage(problem_id, llm, sample_num):
    code_dir = os.path.join(FULL_CODE_BASE_DIR, llm, problem_id)
    module_name = f"{FULL_CODE_BASE_DIR}.{llm}.{problem_id}.sample{sample_num}"  # For --cov= (without .py)
    
    test_file = os.path.join(IMPROVED_TEST_DIR, f"test_{problem_id}_{llm}_sample{sample_num}.py")
    
    if not os.path.exists(code_dir) or not os.path.exists(test_file):
        print(f"Skipping {problem_id} ({llm} sample{sample_num}): Missing code or improved test file.")
        return None  # Skip if files missing
    
    # Command to run pytest with coverage (using improved test file only)
    cmd = [
        'pytest',
        '--cov=' + module_name,
        '--cov-branch',
        '--cov-report=term-missing',
        '--cov-report=html:' + os.path.join(COVERAGE_REPORT_DIR, f"{problem_id}_{llm}_sample{sample_num}_html"),
        '-v',  # Verbose for details
        test_file
    ]
    
    # Set environment with PYTHONPATH to include project root
    project_root = os.getcwd()
    env = os.environ.copy()
    env['PYTHONPATH'] = project_root + (os.pathsep + env.get('PYTHONPATH', ''))
    
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, env=env)
    except subprocess.CalledProcessError as e:
        output = e.output  # Capture output even if error
    
    # Print the full output for debugging
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
    
    # Basic note (customize in PDF)
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

# Collect results for selected samples
results = []
for sel in SELECTED:
    result = run_improved_coverage(sel['problem_id'], sel['llm'], sel['sample_num'])
    if result:
        results.append(result)

# Write to CSV for Part 2 report
if results:
    with open('improved_coverage.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Problem (LLM Sample)', 'Tests Passed', 'Line Coverage %', 'Branch Coverage %', 'Notes'])
        for r in results:
            writer.writerow([r['problem'], r['tests_passed'], r['line_%'], r['branch_%'], r['notes']])
    print("Improved coverage table written to improved_coverage.csv")
else:
    print("No results found for improved tests.")