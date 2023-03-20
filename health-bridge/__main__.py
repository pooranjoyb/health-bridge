import os
os.chdir('health-bridge')
os.system('python -m spacy download en_core_web_sm')
os.system("python main.py")