from info import *
BOT_ADMIN = telebot.TeleBot(TOKEN_BOT_ADD)

def replty_func (message):
    if message.text == "اهلا" :
        BOT_ADMIN.reply_to(message,"اهلين")
    else:
        BOT_ADMIN.reply_to(message,"تم ارسال الرسالة ")
             