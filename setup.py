import os, sys
import subprocess as sp
if sys.platform =="linux":
    os.system('sudo apt-get install scrot wmctrl')
    os.system('sudo pacman -S grim scrot wmctrl')
    sp.run('python3 -m venv bot-env'.split(' '))
    os.system('sh test-env/bin/activate ')
f = open('api','w+')
api_key = input('API:')
f.write(api_key)
os.system("pip install -r requirements.txt --break-system-packages")


os.system('python fix.py')
