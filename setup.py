import os
f = open('api','w+')
api_key = input('API:')
f.write(api_key)
os.system("pip install -r requirements.txt")
os.system('pip3 uninstall telebot')
os.system('pip3 uninstall PyTelegramBotAPI')
os.system('pip3 install PyTelegramBotAPI')
os.system('pip3 install --upgrade PyTelegramBotAPI')