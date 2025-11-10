import json
import os

HUMANEVAL_JSONL = 'human-eval/data/HumanEval.jsonl'
CODE_BASE_DIR = 'generated_code'               # Original samples
FULL_CODE_DIR = 'full_generated_code'          # New folder for full files
LLMS = ['grok', 'chatgpt']
SAMPLES = range(1, 6)

# Limit to first 10 problems: HumanEval/0 to HumanEval/9
DESIRED_TASKS = [f'HumanEval/{i}' for i in range(10)]

os.makedirs(FULL_CODE_DIR, exist_ok=True)

with open(HUMANEVAL_JSONL, 'r') as f:
    for line in f:
        problem = json.loads(line)
        if problem['task_id'] not in DESIRED_TASKS:
            continue
        
        task_id = problem['task_id'].replace('/', '_')  # e.g., 'HumanEval_0'
        prompt = problem['prompt']                      # Full prompt with open docstring
        
        for llm in LLMS:
            llm_dir = os.path.join(FULL_CODE_DIR, llm, task_id)
            os.makedirs(llm_dir, exist_ok=True)
            
            for sample in SAMPLES:
                original_code_path = os.path.join(CODE_BASE_DIR, llm, task_id, f'sample{sample}.py')
                if not os.path.exists(original_code_path):
                    print(f"Skipping {task_id} ({llm} sample{sample}): Missing original code file.")
                    continue
                
                with open(original_code_path, 'r') as f:
                    code = f.read()
                
                # Close the docstring (indented) and append the body
                full_code = prompt + '\n' + code
                
                full_code_path = os.path.join(llm_dir, f'sample{sample}.py')
                with open(full_code_path, 'w') as f:
                    f.write(full_code)

print("Full code files generated in", FULL_CODE_DIR)