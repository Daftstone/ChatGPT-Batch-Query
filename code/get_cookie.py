import os
import pandas as pd
from chatgpt import ChatGPT
import pickle
import warnings

warnings.filterwarnings("ignore")

bot = ChatGPT()

while (True):
    try:
        question = 'hello'
        print(question)
        response = bot.ask(question)
        print(response)
        break
    except Exception as e:
        bot.refresh()
cookies = bot.browser.cookies()
print(cookies)

try:
    with open("cookies.pkl", "rb") as f:
        cookies_his = pickle.load(f)
except:
    cookies_his = []
cookies_his.append(cookies)

for cookie in cookies_his:
    print(cookie)

with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies_his, f)

print("Add account completed!")