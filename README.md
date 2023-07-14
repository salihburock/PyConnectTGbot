PyConnectTelegramBot

1. Create a telegram bot from t.me/botfather (detailed instructions at https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Copy the API Token
3. Run setup.py and paste the API Token
4. Wait for it to download required modules
5. Run main.py (in case it doesn't work run fix.py and try again if it's still broken report an issue)
6. Send a message to your telegram bot Functions for telegram bot:

#nonstoprun.bat runs python scipt in a batch loop so if python script gets terminated it will start again instantly. It will stop if you terminate batch job(named conhost.exe in task manager

#runinbackground.vbs runs nonstoprun.bat without any trace.

**/restart**

Restars the script so any changes can be applied

**/start**

Sends your chat id so you can add it to admins.json

**/ss or /screenshot**

takes a screenshot and sends it through telegram

**/mp or /mouseposition**

takes a screenshot draws a square where mouse is and sends it

**/cam**

captures a photo via camera using opencv

**/moveto**

moves cursor to given coordinates(ex: /moveto 314 159)

**/move**

moves cursor by given values (ex: /move 314 159)

**/click - /rclick**

left - right clicks where cursor is

**/click x y - /rclick x y**

left - right clicks to given coordinates (ex: /click 265 358)

**/doubleclick or /dc**

double clicks where mouse is

**/talk or /tts**

turns text into speech sends .mp3 file and plays the .mp3 file 

**/os or /cmd** 

allows you to run terminal commands

**/titles**

sends titles of running programs using pyautogui's getAllTitles() method

**/press**

presses the given button. Works via pyautogui's press() method (ex: /press win)

**/type**

types the given words. Works via pyautogui's typewrite() method (ex: /type Hello World)

**/nf or /newfile**
Syntax : 
/nf\n
filename\n
file\n
content
