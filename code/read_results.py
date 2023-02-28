import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='CTtest_original', help='input file name')
parser.add_argument('--onechat', type=bool, default=False, help='all questions in a chat or different chats')
args = parser.parse_args()

if (args.onechat == True):
    type = "one_chat"
else:
    type = "different_chat"

for name in [args.dataset]:
    cur_name = f"{name}_{type}"

    dir = f"../result/{cur_name}"
    file_names = os.listdir(dir)
    df = pd.DataFrame(columns=['question'])
    for i, file in enumerate(file_names):
        if ("all_data" not in file):
            cur_file = f"{dir}/{file}"
            cur_data = pd.read_csv(cur_file)
            df["question"] = cur_data['question']
            df['round_%d' % i] = cur_data['answer']
    df.to_csv(f"{dir}/all_data.csv", index=False, encoding="utf-8-sig")
