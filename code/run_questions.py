import os
import pandas as pd
from chatgpt import ChatGPT
from datetime import datetime
import time
import warnings
import pickle
import argparse
from utils import *
import numpy as np

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='CTtest_original', help='input file name')
parser.add_argument('--onechat', type=bool, default=False, help='all questions in a chat or different chats')
args = parser.parse_args()

file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
if (args.onechat):
    if not os.path.isdir(f"../result/{args.dataset}_one_chat"):
        os.makedirs(f"../result/{args.dataset}_one_chat")
    response_file_path = f"../result/{args.dataset}_one_chat/{args.dataset}_response_{file_name}.csv"
else:
    if not os.path.isdir(f"../result/{args.dataset}_different_chat"):
        os.makedirs(f"../result/{args.dataset}_different_chat")
    response_file_path = f"../result/{args.dataset}_different_chat/{args.dataset}_response_{file_name}.csv"

bot = ChatGPT()

try:
    data = pd.read_csv(f"../data/{args.dataset}.csv", encoding='gbk')
except:
    data = pd.read_csv(f"../data/{args.dataset}.csv")

try:
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        print("number of accounts: ", len(cookies))
except:
    cookies = [bot.browser.cookies()]
    print("number of accounts: ", len(cookies))

df = pd.DataFrame(columns=["question", 'answer'])
re_asking = 20

# Account id, indicating which account will be used
try:
    account_id = int(np.load("../result/cur_cookie_id.npy"))
    if (args.onechat):
        account_id = (account_id + 1) % len(cookies)
    bot.change_count(cookies[account_id])
except:
    account_id = 0
print("current account: ", account_id)

question_list = list(data['question'])
try:
    question_id_list = list(data['id'])
except:
    question_id_list = [i for i in range(len(question_list))]
if ('prompt' in data.columns):
    data = data.fillna(method='pad')
    prompt_list = list(data['prompt'])
else:
    prompt_list = ["" for i in range(len(question_list))]

cur_id = -9999
question_block = []
prompt_block = []
for i in range(len(question_list)):
    question_block.append(question_list[i])
    prompt_block.append(prompt_list[i])

    # run a list questions with the same id
    if (i == len(question_list) - 1 or question_id_list[i + 1] != question_id_list[i]):
        response_list = []
        q_id = 0
        while (True):
            question = question_block[q_id]
            prompt = prompt_block[q_id]
            count = 0  # retry times
            while (True):
                count += 1
                if (count == 1):
                    print(f"Q{i + 1}", f"{prompt} {question}")

                try:
                    response = bot.ask(f"{prompt} {question}")
                except Exception as e:
                    response = "Failed to read response"

                if ("Unusable response produced" in response or "Failed to read response" in response or len(
                        response) == 0):
                    if (count > re_asking):
                        print("\n\n")
                        if (args.onechat):
                            print("The current account is wrong. Because it is one chat, we stop and run again.")
                            np.save("../result/cur_cookie_id.npy", account_id)
                            exit(-1)
                        else:
                            # change to an available account
                            print("find an available account")

                            account_id = (account_id + 1) % len(cookies)
                            bot.change_count(cookies[account_id])
                            print(f"change account to {account_id}")

                            count = 0
                            q_id = 0
                            response_list = []
                    else:
                        print("\rre-asking %d times" % count, end="", flush=True)
                        bot.refresh()
                        continue
                else:
                    q_id += 1
                    response_list.append(response)

                if (count == 0):
                    break

                print("\n")
                print(f"R{i + 1}:", response)
                print("\n\n")
                break

            if (q_id == len(question_block)):
                break

        for question, response in zip(question_block, response_list):
            df = df.append({"question": question, "answer": response}, ignore_index=True)
        if (args.onechat == False):
            print("change chat")
            bot.new_conversation()
        question_block = []
        prompt_block = []
    else:
        continue

df.to_csv(response_file_path, index=False, encoding="utf-8-sig")
np.save("../result/cur_cookie_id.npy", account_id)
