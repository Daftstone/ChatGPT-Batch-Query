## About
About
This project is used to automatically grab the query results of ChatGPT in batches without manual input. And it supports automatic switching between multiple accounts. We are using the [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper) library to interact with the ChatGPT API.

## Highlights
* One-click script for Windows, Mac, and Linux, easy for novices.
* Automatic human verfication.
* Automatic switching between multiple accounts when access restrictions are in place (with a limit on queries per hour per account).
* Support multiple categories of input questions.
* Run as a single chat (with all questions asked in one chat).
* Run as multiple chats (with each question asked in a separate chat).

## Install
1. Install python, it is recommended to use Anaconda to install. (Ignore this part if it is already installed)
2. Click install.bat (Windows) or install.command (Mac) or python install.py (Linux) to install the necessary toolkit. A browser window will open during the installation process, and log in to ChatGPT in the browser window. After logging in, the installation of our project is over, and finally closing the browser also closes the script.

## Multiple account support (ignore if only one account)
Due to the limitation of chatgpt, there is an upper limit for each account's query per hour. To this end, our program supports automatic detection of whether the current account has reached the query limit and switches accounts to improve efficiency. If there are multiple accounts, please add multiple accounts as follows (note that each account only needs to be added once and can be reused):
1. Click install.bat (Windows) or install.command (Mac) or python install.py (Linux), a browser interface will pop up, there may be two situations:
   1. Not logged into chatgpt. Then enter the account and password to be added and log in, then close the browser and close the script.
   2. Already logged in. Then click the three bars in the upper right corner of the browser → Settings → Privacy and Security → Manage Data → select openai.com → remove selected → save changes → exit the settings. At this time, refresh the chatgpt webpage again, and it will change to the first situation, that is, the login interface. Enter the account and password to be added and log in, then close the browser and close the script.
2. Click add_account.bat (Windows) or add_account.command (Mac) or python add_account.py (Linux), and "Add account completed!" appears, indicating that the account is added successfully.

## Question set preparation
* Naming and saving: a set of question sets is a file, stored in .csv form, and saved in .\data.
* File specification. The following three types of files are supported:
  * Each question in the question set is independent, so name a column in the table as "question", and then each row represents a question input.
  * Question sets that require a prompt. In addition to the "question" column, a "prompt" column is required, which indicates the prompt for the current question. If all questions share a prompt, you only need to fill in the prompt for the first question.
  * If some questions are related, add another column named id, set the ids of these questions to be the same, and set the ids of unrelated questions to be different.

## Usage
The tool can be used in two ways:
* Use ChatGPT interactively: click run_interactive.bat (Windows) or run_interactive.command (Mac) or python run_interactive.py (Linux), enter the question and reply, and you can interact with ChatGPT (There may be errors in the first run, just run it again).
* Batch input from a file:
  1. A set of questions must be run under the same chat. Then click run_batch_one_chat.bat (or run_batch_one_chat.command or python run_batch_one_chat.py), which will run all the question sets listed in question_list.txt. The result is saved in result/[dataset]_one_chat directory.
  2. Each question runs under a different chat. then click run_batch_different_chat.bat (run_batch_different_chat.command or python run_batch_different_chat.py), which will run all the question sets listed in question_list.txt. The result is saved in result/[dataset]_different_chat directory.
