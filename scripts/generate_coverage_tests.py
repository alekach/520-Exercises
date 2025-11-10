import json
import os

HUMANEVAL_JSONL = 'human-eval/data/HumanEval.jsonl'
TEST_DIR = 'tests'                             # Output folder for test files
FULL_CODE_BASE_DIR = 'full_generated_code'     # Use the new full code folder
LLMS = ['grok', 'chatgpt']
SAMPLES = range(1, 6)

# Limit to first 10 problems: HumanEval/0 to HumanEval/9
DESIRED_TASKS = [f'HumanEval/{i}' for i in range(10)]

os.makedirs(TEST_DIR, exist_ok=True)

with open(HUMANEVAL_JSONL, 'r') as f:
    for line in f:
        problem = json.loads(line)
        if problem['task_id'] not in DESIRED_TASKS:
            continue
        
        task_id = problem['task_id'].replace('/', '_')  # e.g., 'HumanEval_0'
        entry_point = problem['entry_point']            # Function name
        test_code = problem['test']                     # The check function string
        
        # Loop over LLMS and samples to generate unique test files
        for llm in LLMS:
            for sample in SAMPLES:
                # Generate unique test file name
                test_file_path = os.path.join(TEST_DIR, f'test_{task_id}_{llm}_sample{sample}.py')
                
                with open(test_file_path, 'w') as tf:
                    # Import pytest and the candidate function
                    tf.write('import pytest\n\n')
                    tf.write(f'from {FULL_CODE_BASE_DIR}.{llm}.{task_id}.sample{sample} import {entry_point} as candidate\n\n')
                    
                    # Write the original test code (includes imports and def check)
                    tf.write(test_code + '\n\n')
                    
                    # Add the pytest wrapper
                    tf.write('def test_check():\n')
                    tf.write('    check(candidate)\n')

print("Updated test files generated in", TEST_DIR)