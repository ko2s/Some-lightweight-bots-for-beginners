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
from paddleocr import PaddleOCR
import re
import requests
import json
import pytz
import time
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
import random
import string
from sympy import sympify
from bs4 import BeautifulSoup
import uuid
import segno
from PIL import Image
import pytesseract
load_dotenv()
admin_aq = os.getenv("AdminUser")
Token = os.getenv("Token")
bot = telebot.TeleBot(Token)
developer = int(admin_aq)
boen = os.getcwd()
folder_json = os.getenv("folder_json")
f_path = os.path.join(boen,folder_json)
cred = credentials.Certificate(folder_json)
url_firbass = os.getenv("linkDatabese")
url_storg = os.getenv("link")
firebase_admin.initialize_app(cred, {'databaseURL': url_firbass,'storageBucket': url_storg})
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
libya_timezone = timezone(timedelta(hours=2)) 
created_at = datetime.now(pytz.utc).astimezone(libya_timezone).strftime('%Y-%m-%d %I:%M %p')
user_chat_admin = []
admin = [984370413]
start_text = []
warnings = {}