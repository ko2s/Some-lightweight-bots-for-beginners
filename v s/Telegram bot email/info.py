
import telebot
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telebot.types import Message
load_dotenv()

TOKEN_BOT_ADD = os.getenv('BOT_TOKEN_end')
admin_chat = os.getenv('admin_id_chat')
admin_chat = int(admin_chat)
telebot.TeleBot(TOKEN_BOT_ADD)