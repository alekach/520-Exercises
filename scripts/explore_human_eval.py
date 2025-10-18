from human_eval.data import read_problems

problems = read_problems()

for i in range(0,10):
    problem = problems[f'HumanEval/{i}']
    print("Task ID:", problem['task_id'])
    print("Prompt:", problem['prompt'])  # paste to models
    print("\n")