import os
import telebot
from telebot.types import *
from telebot import types
from telebot.apihelper import ApiTelegramException,ApiException
from datetime import datetime, timezone,timedelta
import threading
import firebase_admin
from firebase_admin import credentials, db,storage
from dotenv import load_dotenv
import re
import requests
import json
import pytz
import emoji
import time
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
import random
import string
from sympy import sympify
from bs4 import BeautifulSoup
import uuid
import segno
boen = os.getcwd()
# os.listdir(boen)
load_dotenv()
end_time = None
user_captcha = {}
photo_url = []
boten_neame_text = {}
message_ass = []
message_ass1 = []
markup_key = []
fldars = []
boten_neame = []
rednmper = []
text_boten = []
chat_ida = []
commandd = []
emoji_list = []
emoji_list1 = []
reeply = []
send = []
calld = []
Button = []
KeyButton = []
keyls = []
Valuels = []
start_text = []
sand_all = []
channels = []
reply_ms = []
timers = []
user_list = []
user_chat_id = []
massage_edita = []
developer = os.getenv('Developer')
developer = int(developer)
admin = [developer]
candidates1 = {}
user_votes2 = {}
user_chat_admin = []
admin_stretor = []
user_list1 = []
name_user1 = []
markup_key1 = []
kasamem = []
section = []
sec_nmper = []
vote_icon = ["🔥"]
call_data = []
message_msid = []
user_messages = {}
candidate_name_key = []
key_keu = []
مسار_الصورة = []
user_votes = defaultdict(lambda: None)
user_captcha_okke = defaultdict(lambda: None)
candidates = {}
banned_users = set()
token = os.getenv('TOKEN_BOT')
url_db = os.getenv('url_firbass')
url_storgs = os.getenv("url_storg")
bot = telebot.TeleBot(token)
libya_timezone = timezone(timedelta(hours=2)) 
# تحديد الوقت الحالي بالتوقيت العالمي (UTC)
# created_at = datetime.now(pytz.utc).astimezone(libya_timezone).isoformat()
created_at = datetime.now(pytz.utc).astimezone(libya_timezone).strftime('%Y-%m-%d %I:%M %p')
# تهيئة Firebase
folder_json = "bot-b35e9-firebase-adminsdk-c8nlo-be90ee50c4.json"
f_path = os.path.join(boen,folder_json)
cred = credentials.Certificate(folder_json)
lset = True
fast_run = False
ts = False
photo = "photo"
voice =  'voice'
audio =  "audio"
document = "document"
sticker =  "sticker"
video =  "video"
video_note =  "video_note"
location =  "location"
contact =  "contact"
op_close = {
    "photo": "photo",
    "voice": 'voice',
    "audio": "audio",
    "document": "document",
    "sticker": "sticker",
    "video": "video",
    "video_note": "video_note",
    "location": "location",
    "contact": "contact",
}
name_op = {
    photo: "صور",
    voice: "صوت",
    audio: "مقطع صوتي",
    document: "مستند",
    sticker: "ملصق",
    video: "فيديو",
    video_note: "ملاحظة فيديو",
    location: "موقع",
    contact: "جهة اتصال",
}
mtargam = {
    "🔓 فتح" : "مقفل 🔒",
    "🔒 قفل" : "مفتوح 🔓",
}
name_op_values = ["صور","صوت","مقطع صوتي","مستند","ملصق","فيديو","ملاحظة فيديو","موقع","جهة اتصال"]
close = []
xc = ["photo_op","voice_op","audio_op","document_op","sticker_op","video_op","video_note_op","location_op","contact_op","text_op","photo_close","voice_close","audio_close","document_close","sticker_close","video_close","video_note_close","location_close","contact_close","text_close"]
firebase_admin.initialize_app(cred, {
    'databaseURL': url_db,
    'storageBucket': url_storgs

})

headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Length': '25',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

boten_key_name = {
    "add_user"  : 'اضافة متسابق',
    "delet_user": 'حذف متسابق',
    "add_admin" : 'اضافة ادمن',
    "delet_admin": 'حذف ادمن',
    "view_vote" : 'الإحصائية 📊',
    "settings"  : 'اعدادات البوت',
    "add_button_key": '🏁بداء المسابقة 🏁',
    "stop_key": "🛑 إيقاف المسابقة 🛑"
}
def send_admin_panel(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕ إضافة متسابق", callback_data="add_candidate"))
    markup.add(InlineKeyboardButton(f"🔄 تغيير أيقونة التصويت (حاليًا: {vote_icon[0]})", callback_data="change_icon1"))
    markup.add(InlineKeyboardButton("حذف قسم 🗑", callback_data="dlet_sec"))
    markup.add(InlineKeyboardButton("➕ إضافة قسم", callback_data="add_section"))
    bot.send_message(chat_id, "🔧 لوحة التحكم:", reply_markup=markup)
       
#يتم استرجعها من ملف main
def main_callbacd(call):
    user_id = call.from_user.id
    chat_id = user_id
    if call.data == "photo_op":
        photo = "None"
        op_close.update({"photo" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values[0])} بنجاح 🔓✅")
    elif call.data == "voice_op":      
        voice = "None"
        op_close.update({"voice" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[1]} بنجاح 🔓✅")
    elif call.data == "audio_op":      
        audio = "None"
        op_close.update({"audio" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[2]} بنجاح 🔓✅")
    elif call.data == "document_op":   
        document = "None"
        op_close.update({"document" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[3]} بنجاح 🔓✅")
    elif call.data == "sticker_op":    
        sticker = "None"
        op_close.update({"sticker" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[4]} بنجاح 🔓✅")
    elif call.data == "video_op":      
        video = "None"
        op_close.update({"video" : "None"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[5]} بنجاح 🔓✅")
    elif call.data == "video_note_op": 
        video_note = "None"
        op_close.update({"video_note" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[6]} بنجاح 🔓✅")
    elif call.data == "location_op":
        location = "None"
        op_close.update({"location" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[7]} بنجاح 🔓✅")
    elif call.data == "contact_op":
        contact = "None"
        op_close.update({"contact" : "None"})
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم فتح {(name_op_values)[8]} بنجاح 🔓✅")
    elif call.data == "photo_close":
        photo = "photo"
        op_close.update({"photo" : "photo"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[0]} بنجاح 🔒✅")
    elif call.data == "voice_close":
        voice = "voice"
        op_close.update({"voice" : "voice"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[1]} بنجاح 🔒✅")
    elif call.data == "audio_close":
        audio = "audio"
        op_close.update({"audio" : "audio"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[2]} بنجاح 🔒✅")
    elif call.data == "document_close":
        document = "document"
        op_close.update({"document" : "document"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[3]} بنجاح 🔒✅")
    elif call.data == "sticker_close":
        sticker = "sticker"
        op_close.update({"sticker" : "sticker"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[4]} بنجاح 🔒✅")
    elif call.data == "video_close":
        video = "video"
        op_close.update({"video" : "video"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[5]} بنجاح 🔒✅")
    elif call.data == "video_note_close":
        video_note = "video_note"
        op_close.update({"video_note" : "video_note"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[6]} بنجاح 🔒✅")
    elif call.data == "location_close":
        location = "location"
        op_close.update({"location" : "location"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[7]} بنجاح 🔒✅")
    elif call.data == "contact_close":
        contact = "contact"
        op_close.update({"contact" : "contact"})
        
        try:
            keyboard = InlineKeyboardMarkup()
            for key , value in op_close.items():
                
            
                if value == "None":
                    btn1 = InlineKeyboardButton(text= "🔒 قفل", callback_data=f'{key}_close')
                    close.append("🔒 قفل")
                else:
                    
                    btn1 = InlineKeyboardButton(text= "🔓 فتح", callback_data=f'{key}_op')
                    close.append("🔓 فتح")
                keyboard.add(btn1,InlineKeyboardButton(text=name_op.get(key), callback_data='k'))
            masge_text = f"""
لوحة تحكم قفل وفتح الخصائص \n🔒 : قفل الخصائص \n🔓 : فتح الخصائص
حالة الصور : {mtargam.get(close[0])}🖼
حالة صوت : {mtargam.get(close[1])}🎙
حالة مقطع صوتي : {mtargam.get(close[2])}🎶
حالة مستند : {mtargam.get(close[3])}📁
حالة ملصق : {mtargam.get(close[4])}🌅
حالة فيديو : {mtargam.get(close[5])}🎬
حالة ملاحظة فيديو : {mtargam.get(close[6])}📹
حالة موقع : {mtargam.get(close[7])}🗺️
حالة جهة اتصال : {mtargam.get(close[8])}☎️
"""
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text =masge_text,reply_markup=keyboard)
        except:
               pass
        bot.answer_callback_query(call.id, f"تم قفل {(name_op_values)[8]} بنجاح 🔒✅")