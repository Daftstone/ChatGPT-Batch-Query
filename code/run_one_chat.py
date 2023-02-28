import os

file_list = []
time_list = []
with open("../question_list.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.split(",")
        file_list.append(a)
        time_list.append(int(b))

for dataset, times in zip(file_list, time_list):
    count = 0
    while (count < times):
        flag = os.system(f"python run_questions.py --dataset {dataset} --onechat True")
        if (flag == 0):
            count += 1
    os.system(f"python read_results.py --dataset {dataset} --onechat True")

print("\nEnd of Run!!!")