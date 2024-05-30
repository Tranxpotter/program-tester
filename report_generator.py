import os
import json

results_folder = input("Generate results for (folder name - datetime): ")

results_path = f"results/{results_folder}/results.json"

if not os.path.exists(results_path):
    raise ValueError(f"Cannot find results from {results_path}")

os.makedirs(f"reports/{results_folder}", exist_ok=True)

with open(results_path, "r") as f:
    results = json.load(f)

scores = {}
ranks = {}

#Generate report for each participant
for participant, result in results.items():
    report = ""
    #Calculate total score
    total_score = 0
    for task, test_cases in result.items():
        for test_case in test_cases:
            if test_case["is_correct"]:
                total_score += 1                #Add to score for each passed test case
            
        if all([test_case["is_correct"] for test_case in test_cases]):
            total_score += 5                    #Add to score for all test cases passed in a task
        
    scores[participant] = total_score
    report += f"**total score: {total_score}**\n-------------------------------\n"""
    
    #Generate detailed report for each task
    for task, test_cases in result.items():
        report += f"task {task}:\n-------------------------------\ncase |      status      |       time (s)       |note\n"
        for index, test_case in enumerate(test_cases):
            report += f"{index+1:>5}|"
            if test_case["is_correct"]:
                report += f"{'Correct Answer':^18}|"
            elif test_case["error_type"]:
                report += f"{test_case['error_type']:^18}|"
            else:
                report += f"{'Wrong Answer':^18}|"
            
            report += f"{test_case['execution_time']:^22}|"
            error_msg = test_case['error_msg'].replace('\n', ' ')
            report += f"{error_msg}\n"
    
    with open(f"reports/{results_folder}/{participant}.txt", "w") as f:
        f.write(report)

scores = dict(sorted(scores.items(), key=lambda x:x[1], reverse=True))
leaderboard = "rank|       participant       | score \n"
for index, (participant, score) in enumerate(scores.items()):
    leaderboard += f"{index+1:>4}|{participant:^25}|{score:^7}\n"

with open(f"reports/{results_folder}/leaderboard.txt", "w") as f:
    f.write(leaderboard)













