from info import *
from replt import *
BOT_ADMIN = telebot.TeleBot(TOKEN_BOT_ADD)

@BOT_ADMIN.message_handler(func= lambda message : True)
def rm (message):
    replty_func(message)

BOT_ADMIN.infinity_polling()