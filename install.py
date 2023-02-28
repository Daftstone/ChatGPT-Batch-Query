import os
import sys

sys.path.append("code")
os.system("pip install pytest-playwright rich pyreadline3")
os.system("playwright install firefox")
os.system("cd code && python main.py install")
