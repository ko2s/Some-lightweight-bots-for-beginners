@bot.callback_query_handler(func=lambda call: call.data == 'stats')
def show_statistics(call):
    try:
        total_users = len(user_ids)
        bot.send_message(call.message.chat.id, f"(———————————)\n\nاحصائيات بوتك :\nعدد المستخدمين : {total_users}\n\n(———————————)")
    except Exception as e:
        logging.error(f"Error in show_statistics: {e}")
        bot.send_message(call.message.chat.id, "⚠️ حدث خطأ أثناء عرض الإحصائيات.")
@bot.callback_query_handler(func=lambda call: call.data == 'send_private_message')
def request_user_id_for_message(call):
    bot.send_message(call.message.chat.id, "📝 أدخل معرف المستخدم أو الـID للشخص الذي تريد إرسال رسالة إليه:")
    bot.register_next_step_handler(call.message, get_user_id_for_message)

def get_user_id_for_message(message):
    user_id_or_username = message.text.strip().lstrip('@')
    if user_id_or_username:
        if is_user_in_bot(user_id_or_username):
            bot.send_message(message.chat.id, "📨 أدخل الرسالة التي تريد إرسالها:")
            bot.register_next_step_handler(message, process_and_send_message, user_id_or_username)
        else:
            bot.send_message(message.chat.id, f"❌ تعذر العثور على المستخدم {user_id_or_username}. تأكد من إدخال الاسم أو الـID بشكل صحيح.")
    else:
        bot.send_message(message.chat.id, "⚠️ لم يتم إدخال معرف مستخدم صالح.")

def process_and_send_message(message, user_id_or_username):
    msg = message.text.strip()
    if not msg:
        bot.send_message(message.chat.id, "⚠️ لم يتم إدخال رسالة صالحة.")
        return

    try:
        chat_id = None
        if user_id_or_username.isdigit():
            chat_id = int(user_id_or_username)
        else:
            chat_id = next((cid for cid, info in bot_scripts.items() if info.get('uploader', '').lower() == user_id_or_username.lower()), None)

        if chat_id:
            bot.send_message(chat_id, msg)
            bot.send_message(message.chat.id, "✅ تم إرسال الرسالة بنجاح.")
        else:
            bot.send_message(message.chat.id, f"❌ تعذر العثور على المستخدم {user_id_or_username}. تأكد من إدخال الاسم أو الـID بشكل صحيح.")
    except Exception as send_error:
        logging.error(f"Error sending message to {user_id_or_username}: {send_error}")
        bot.send_message(message.chat.id, f"⚠️ حدث خطأ أثناء إرسال الرسالة إلى المستخدم {user_id_or_username}.")

def is_user_in_bot(username_or_id):
    """ تحقق مما إذا كان المستخدم موجودًا في بيانات البوت """
    if username_or_id.isdigit():
        return int(username_or_id) in bot_scripts
    else:
        return any(info.get('uploader', '').lower() == username_or_id.lower() for info in bot_scripts.values())
@bot.callback_query_handler(func=lambda call: call.data == 'create_qr')
def ask_for_qr_text(call):
    bot.send_message(call.message.chat.id, "📝 ادخل نص لوضعه في رمز QR:")

    # تسجيل الخطوة التالية لانتظار إدخال المستخدم
    bot.register_next_step_handler(call.message, generate_qr)

def generate_qr(message):
    qr_text = message.text.strip()
    try:
        # إنشاء رمز QR باستخدام segno بجودة عالية
        qr = segno.make(qr_text)
        qr_file = "qr_code.png"
        qr.save(qr_file, scale=10)  # تحسين الجودة باستخدام scale

        # إرسال رمز QR للمستخدم
        with open(qr_file, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        # حذف الملف بعد الإرسال
        os.remove(qr_file)

    except Exception as e:
        bot.send_message(message.chat.id, "❌ حدث خطأ أثناء إنشاء رمز QR. تأكد من أنك أدخلت نصًا صالحًا.")
@bot.callback_query_handler(func=lambda call: call.data == 'fetch_html')
def request_html_url(call):
    if is_user_blocked(call.from_user.id):
        bot.answer_callback_query(call.id, BLOCKED_MESSAGE)
        return

    # تحديث حالة الجلسة إلى 'fetch_html'
    update_user_session(call.from_user.id, 'fetch_html')
    bot.send_message(call.message.chat.id, "يرجي العلم ان مش كل الصفح بيتم سحبها بسبب عدم قدره البوت في جلب المحتوا\n 📝 أدخل رابط الصفحة لسحب هيكل الـ HTML:")
    bot.register_next_step_handler(call.message, fetch_html)

def fetch_html(message):
    if not is_in_session(message.from_user.id, 'fetch_html'):
        return
    url = message.text.strip()
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        html_content = soup.prettify()

        file_name = "page.html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_content)

        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)

        os.remove(file_name)

    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء جلب الـ HTML: {str(e)}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ: {str(e)}")
@bot.callback_query_handler(func=lambda call: call.data == 'create_files')
def create_files(call):
    if is_user_blocked(call.from_user.id):
        bot.answer_callback_query(call.id, BLOCKED_MESSAGE)
        return

    # تحديث حالة الجلسة إلى 'create_files'
    update_user_session(call.from_user.id, 'create_files')
    
    bot.send_message(call.message.chat.id, "من هنا يمكنك صنع ملفات.\nاختر صيغة الملفات من الأسفل:", reply_markup=file_format_markup())

def file_format_markup():
    markup = types.InlineKeyboardMarkup()
    txt_button = types.InlineKeyboardButton(".txt", callback_data='create_txt')
    py_button = types.InlineKeyboardButton(".py", callback_data='create_py')
    env_button = types.InlineKeyboardButton(".env", callback_data='create_env')
    markup.add(txt_button, py_button, env_button)
    return markup

########## دالة طلب محتوى الملف ##########

@bot.callback_query_handler(func=lambda call: call.data in ['create_txt', 'create_py', 'create_env'])
def request_file_content(call):
    if not is_in_session(call.from_user.id, 'create_files'):
        return
    file_format = call.data.split('_')[1]

    # تحديث حالة الجلسة إلى 'create_{file_format}'
    update_user_session(call.from_user.id, f'create_{file_format}')
    
    bot.send_message(call.message.chat.id, f"📝 أدخل محتوى الملف بصيغة {file_format} لحفظه:")
    bot.register_next_step_handler(call.message, lambda msg: save_file(msg, file_format))

########## دالة حفظ الملف ##########

def save_file(message, file_format):
    if not is_in_session(message.from_user.id, f'create_{file_format}'):
        return
    content = message.text
    file_name = f"file.{file_format}"

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)

        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(file_name)
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء حفظ الملف: {str(e)}")
@bot.callback_query_handler(func=lambda call: call.data == 'check_speed')
def check_speed(call):
    bot.send_message(call.message.chat.id, "⏳ انتظر، يتم قياس سرعة البوت...")

    # قياس سرعة البوت
    start_time = time.time()
    # يمكن استخدام أي عملية بسيطة لقياس السرعة، مثل إرسال واستقبال رسالة
    bot.send_message(call.message.chat.id, "جاري قياس السرعة...")
    response_time = time.time() - start_time

    # تحويل الزمن إلى ميلي ثانية
    response_time_ms = response_time * 1000

    # تقييم السرعة
    if response_time_ms < 100:
        speed_feedback = f"سرعة البوت الحالية: {response_time_ms:.2f} ms - ممتازه !⚡️"
    elif response_time_ms < 300:
        speed_feedback = f"سرعة البوت الحالية: {response_time_ms:.2f} ms - جيد جدا ✨🙂"
    else:
        speed_feedback = f"سرعة البوت الحالية: {response_time_ms:.2f} ms - يجب تحسين الإنترنت ❌"

    bot.send_message(call.message.chat.id, speed_feedback)

@bot.callback_query_handler(func=lambda call: call.data == 'suggest_modification')
def suggest_modification(call):
    bot.send_message(call.message.chat.id, "💡 اكتب اقتراحك الآن، أو أرسل صورة أو ملف وسأرسله للمطور.")
    bot.register_next_step_handler(call.message, handle_suggestion)

def handle_suggestion(message):
    if message.text:
        bot.send_message(ADMIN_ID, f"💡 اقتراح من @{message.from_user.username}:\n\n{message.text}")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك بنجاح للمطور!")
    elif message.photo:
        photo_id = message.photo[-1].file_id  # الحصول على أكبر صورة
        bot.send_photo(ADMIN_ID, photo_id, caption=f"💡 اقتراح من @{message.from_user.username} (صورة)")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك كصورة للمطور!")
    elif message.document:
        file_id = message.document.file_id
        bot.send_document(ADMIN_ID, file_id, caption=f"💡 اقتراح من @{message.from_user.username} (ملف)")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك كملف للمطور!")
    else:
        bot.send_message(message.chat.id, "❌ لم يتم تلقي أي محتوى. يرجى إرسال الاقتراح مرة أخرى.")
if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(5)  # انتظار 5 ثواني قبل إعادة المحاولة             