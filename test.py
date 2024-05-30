import json
import os
folders = os.listdir("results")
paths = []
for folder in folders:
    paths.append(f"results/{folder}/results.json")
    
for path in paths:
    with open(path, "r") as f:
        results:dict = json.load(f)

    times = []
    for participant, tasks in results.items():
        total_time = 0
        for task, runs in tasks.items():
            for run in runs:
                execution_time = run["execution_time"]
                total_time += execution_time
        times.append(total_time)
        # print(f"{participant}: {total_time}")
    print(f"time diff (your method total time - my method total time): {times[0]-times[1]}")