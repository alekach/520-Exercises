import os

FULL_CODE_DIR = 'full_generated_code'  # Folder with full code files
LLMS = ['grok', 'chatgpt']
PROBLEMS = [f'HumanEval_{i}' for i in range(10)]

# Add __init__.py to root full_generated_code
init_path = os.path.join(FULL_CODE_DIR, '__init__.py')
if not os.path.exists(init_path):
    open(init_path, 'w').close()

# Add to each LLM and problem subfolder
for llm in LLMS:
    llm_dir = os.path.join(FULL_CODE_DIR, llm)
    init_path = os.path.join(llm_dir, '__init__.py')
    if not os.path.exists(init_path):
        open(init_path, 'w').close()
    
    for problem_id in PROBLEMS:
        problem_dir = os.path.join(llm_dir, problem_id)
        init_path = os.path.join(problem_dir, '__init__.py')
        if not os.path.exists(init_path):
            open(init_path, 'w').close()

print("Added __init__.py files to make directories importable.")