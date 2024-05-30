import subprocess
import time
import os
import datetime
import json
import timeit
from typing import Callable


def execute_script(script_path, input):
    #Add traceback disabling code
    with open(script_path, "r") as f:
        code = f.read()
    code = "import sys\nsys.tracebacklimit=0\n" + code
    
    with open("temp_script.py", "w") as f:
        f.write(code)
    
    # Execute the script and capture its output
    process = subprocess.Popen(['python', "temp_script.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    error_type = ""
    output = ""
    
    start_time = time.time()  # Record the start time
    try:
        output, errs = process.communicate(input=input, timeout=60)
    except subprocess.TimeoutExpired as e:
        execution_time = 60.0
        error_type = "Timeout Error"

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    
    if errs:
        if "SyntaxError" in errs:
            error_type = "Syntax Error"
        else:
            error_type = "Runtime Error"
    
    return output, error_type, errs, execution_time

def default_autofix(user_answer:str, correct_answer:str) -> tuple[str, str]:
    return user_answer.rstrip(), correct_answer.rstrip()

def task1_autofix(user_answer:str, correct_answer:str) -> tuple[str, str]:
    return "\n".join([line.rstrip(line) for line in user_answer.splitlines()]), "\n".join([line.rstrip(line) for line in correct_answer.splitlines()])

def check_answer(user_answer:str, correct_answer:str, autofix:bool = False, autofix_func:Callable[[str, str], tuple[str, str]] = default_autofix) -> bool:
    if autofix:
        user_answer, correct_answer = autofix_func(user_answer, correct_answer)
    return user_answer == correct_answer


if __name__ == "__main__":
    #Save test time
    test_datetime = datetime.datetime.now().replace(microsecond=0)
    test_datetime = test_datetime.isoformat().replace("-", "_").replace(":", "_")
    
    logs = ""
    results = {}
    #Loop through each program
    #----------------- Change Here ----------------------
    for input_program_path in os.listdir("input_programs"):
        try:
            candidate_num, _, task_num = input_program_path.replace(".py", "").split("_")
            task_num = task_num[0]
        except Exception as e:
            print(f"File name error: {input_program_path}")
            logs += f"File name error: {input_program_path}\n"
            continue
        print(f"testing {input_program_path}")
        #-----------------------------------------------------
        
        #Load test cases
        if not os.path.exists(f"inputs/{task_num}"):
            print(f"Cannot find input for task num [{task_num}] for file name [{input_program_path}]")
            logs += f"Cannot find input for task num [{task_num}] for file name [{input_program_path}]\n"
            continue
        
        if not os.path.exists(f"outputs/{task_num}"):
            print(f"Cannot find output for task num [{task_num}] for file name [{input_program_path}]")
            logs += f"Cannot find output for task num [{task_num}] for file name [{input_program_path}]\n"
            continue
            
        input_paths = os.listdir(f"inputs/{task_num}")
        output_paths = os.listdir(f"outputs/{task_num}")
        cases_results = []
        for input_path, output_path in zip(input_paths, output_paths):
            with open(f"inputs/{task_num}/{input_path}", "r") as f:
                input = f.read()
            
            with open(f"outputs/{task_num}/{output_path}", "r") as f:
                output = f.read()

            print(f"Testing with test case {input_path} | {output_path}")
            #Start testing
            user_output, error_type, error_msg, execution_time = execute_script(f"input_programs/{input_program_path}", input)
            
            if not error_type:
                is_correct = check_answer(user_output, output, autofix=True)    #Toggle autofix here
            else:
                is_correct = False
            
            #Store result
            cases_results.append({
                "is_correct":is_correct, 
                "error_type":error_type,
                "error_msg":error_msg,
                "execution_time":execution_time, 
                "output":user_output,
                "answer":output
            })
    
        if results.get(candidate_num):
            results[candidate_num][task_num] = cases_results
        else:
            results[candidate_num] = {task_num:cases_results}
    
    os.mkdir(f"results/{test_datetime}")
    with open(f"results/{test_datetime}/results.json", "w") as f:
        json.dump(results, f, indent=4)
    with open(f"results/{test_datetime}/logs.txt", "w") as f:
        f.write(logs)
    
    print(f"Result written in {test_datetime}")

