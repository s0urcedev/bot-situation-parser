#imports-----------------------------------
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import telethon
from telethon import TelegramClient, events, utils
import asyncio
#------------------------------------------

#api settings------------------------------
api_id = 12964878 #your account api_id (You can find it on my.telegram.org)
api_hash = '133b369b94c5e14a68a20bd767bcea9b' #your account api_hash (You can find it on my.telegram.org)
channels = [1659763460, 1396104646, 1105313000, 1280273449] #channel's ids which you will parse
#------------------------------------------

def send_email(message_text, channel_name): #arg1 - message text, arg2 - subject

    #creating message----------------------
    msg = MIMEMultipart()
    password = "mrbotUKR" #password from your email account
    msg['From'] = "mrbotUKRAINE@gmail.com" #your email
    msg['To'] = "380966614975@sms.kyivstar.net" #email to whom you will send
    msg['Subject'] = channel_name #subject
    msg.attach(MIMEText(message_text, 'plain')) #adding text to email
    #--------------------------------------

    #server part and sending---------------
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password) #logging
    server.sendmail(msg['From'], msg['To'], msg.as_string()) #sending
    server.quit()
    #--------------------------------------


#creating client---------------------------
client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")
#------------------------------------------

#catching message--------------------------
@client.on(events.NewMessage(chats = channels))
async def my_event_handler(event):
    if event.message:
        print(event.message.message + "\n-----")
        send_email(event.message.message, utils.get_display_name(event.chat if event.chat else (await event.get_chat())))
#------------------------------------------

#client working----------------------------
client.start()
client.run_until_disconnected()
#------------------------------------------
