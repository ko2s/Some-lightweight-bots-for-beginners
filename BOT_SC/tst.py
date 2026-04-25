import telebot
from collections import defaultdict
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7499160659:AAEGoG3YI71ANWO8iAh6CfamkfukohkLWaY'  # ضع توكن البوت هنا
bot = telebot.TeleBot(TOKEN)

# قائمة المتسابقين (يتم حفظها كقاموس يحتوي على اسم المتسابق، قسمه، عدد الأصوات)
candidates = {}
user_votes = defaultdict(lambda: None)

# تخزين المتسابقين لكل قسم
sections = []

# معرف الأدمن (يمكنك تغيير معرف الأدمن هنا)
ADMIN_ID = 984370413  # ضع معرف الأدمن هنا

# أيقونة التصويت (افتراضيًا نار 🔥)
vote_icon = "🔥"

# خطوة إدخال اسم المتسابق
adding_candidate_step = {}

# قائمة الحظر
banned_users = set()

# دالة لإرسال لوحة التحكم للأدمن
def send_admin_panel(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕ إضافة متسابق", callback_data="add_candidate"))
    markup.add(InlineKeyboardButton(f"🔄 تغيير أيقونة التصويت (حاليًا: {vote_icon})", callback_data="change_icon"))
    markup.add(InlineKeyboardButton("🟢 بدء المسابقة", callback_data="start_competition"))
    markup.add(InlineKeyboardButton("➕ إضافة قسم", callback_data="add_section"))
    bot.send_message(chat_id, "🔧 لوحة التحكم:", reply_markup=markup)

# دالة لتحديث أزرار التصويت بعد التصويت
def update_vote_buttons(chat_id, message_id, candidate_key):
    try:
        candidate = candidates[candidate_key]
        markup = InlineKeyboardMarkup()
        vote_button = InlineKeyboardButton(f"{vote_icon} {candidate['votes']}", callback_data=f"vote_{candidate_key}")
        markup.add(vote_button)
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)
    except Exception as e:
        print(f"Error in update_vote_buttons: {e}")

# التحقق من الحسابات الوهمية والبوتات
def is_bot_or_fake(user):
    if user.is_bot:
        return True
    if user.language_code != 'ar':
        return True
    return False

# دالة لعرض المتسابقين عند بدء المستخدم
def send_candidates_list(chat_id):
    if not candidates:
        bot.send_message(chat_id, "لا يوجد متسابقون حاليًا.")
        return

    for candidate_name, candidate_data in candidates.items():
        try:
            markup = InlineKeyboardMarkup()
            vote_button = InlineKeyboardButton(f"{vote_icon} {candidate_data['votes']}", callback_data=f"vote_{candidate_name}")
            markup.add(vote_button)
            bot.send_message(chat_id, f"📛 <b>{candidate_name}</b>\n🔰 القسم: {candidate_data['section']}\n🗳 عدد الأصوات: {candidate_data['votes']}", parse_mode="HTML", reply_markup=markup)
        except Exception as e:
            print(f"Error in send_candidates_list: {e}")

# أوامر الإدمن
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id == ADMIN_ID:
        send_admin_panel(message.chat.id)
    else:
        bot.reply_to(message, "🚫 ليس لديك صلاحيات الوصول إلى لوحة التحكم.")

# بدء المسابقة
@bot.callback_query_handler(func=lambda call: call.data == "start_competition")
def start_competition(call):
    if call.from_user.id == ADMIN_ID:
        try:
            bot.send_message(call.message.chat.id, "🎉 تم بدء المسابقة! يمكن للمستخدمين الآن التصويت.")
            # يمكن إضافة أي إجراءات إضافية هنا لبدء المسابقة
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء بدء المسابقة: {e}")
    else:
        bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات لبدء المسابقة.")

# إضافة متسابق
@bot.callback_query_handler(func=lambda call: call.data == "add_candidate")
def add_candidate(call):
    if call.from_user.id == ADMIN_ID:
        try:
            bot.send_message(call.message.chat.id, "🔤 أرسل اسم المتسابق:")
            adding_candidate_step[call.from_user.id] = 'name'
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء إضافة المتسابق: {e}")
    else:
        bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات لإضافة متسابق.")

@bot.message_handler(func=lambda message: message.from_user.id in adding_candidate_step)
def handle_candidate_steps(message):
    try:
        step = adding_candidate_step[message.from_user.id]
        
        if step == 'name':
            candidates[message.text] = {"name": message.text, "votes": 0, "section": None}
            bot.send_message(message.chat.id, f"🗂 أرسل القسم الذي يتبع له المتسابق {message.text}:")
            adding_candidate_step[message.from_user.id] = 'section'
            adding_candidate_step['current_candidate'] = message.text
        
        elif step == 'section':
            section = message.text
            candidate_name = adding_candidate_step['current_candidate']
            candidates[candidate_name]['section'] = section
            bot.send_message(message.chat.id, f"✅ تم إضافة المتسابق {candidate_name} في قسم {section}.")
            sections.append(section)
            adding_candidate_step.pop(message.from_user.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ أثناء إضافة المتسابق: {e}")

# تغيير أيقونة التصويت
@bot.callback_query_handler(func=lambda call: call.data == "change_icon")
def change_vote_icon(call):
    if call.from_user.id == ADMIN_ID:
        try:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔥", callback_data="icon_🔥"))
            markup.add(InlineKeyboardButton("❤️", callback_data="icon_❤️"))
            bot.send_message(call.message.chat.id, "🔄 اختر الأيقونة الجديدة:", reply_markup=markup)
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء تغيير الأيقونة: {e}")
    else:
        bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات تغيير الأيقونة.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("icon_"))
def set_vote_icon(call):
    global vote_icon
    try:
        vote_icon = call.data.split("_")[1]
        bot.answer_callback_query(call.id, f"✅ تم تغيير الأيقونة إلى {vote_icon}.")
        send_admin_panel(call.message.chat.id)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ أثناء تغيير الأيقونة: {e}")

# إضافة قسم جديد
@bot.callback_query_handler(func=lambda call: call.data == "add_section")
def add_section(call):
    if call.from_user.id == ADMIN_ID:
        try:
            bot.send_message(call.message.chat.id, "🔤 أرسل اسم القسم الجديد:")
            adding_candidate_step[call.from_user.id] = 'new_section'
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء إضافة القسم: {e}")
    else:
        bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات لإضافة قسم.")

@bot.message_handler(func=lambda message: adding_candidate_step.get(message.from_user.id) == 'new_section')
def handle_new_section(message):
    try:
        section = message.text
        sections.append(section)
        bot.send_message(message.chat.id, f"✅ تم إضافة القسم {section}.")
        adding_candidate_step.pop(message.from_user.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ أثناء إضافة القسم: {e}")

# التعامل مع التصويت
@bot.callback_query_handler(func=lambda call: call.data.startswith("vote_"))
def handle_vote(call):
    user_id = call.from_user.id
    candidate_key = call.data.split("_")[1]
    
    if is_bot_or_fake(call.from_user):
        bot.answer_callback_query(call.id, "🚫 لا يمكنك التصويت. حسابك محظور.", show_alert=True)
        banned_users.add(user_id)
        return

    # إذا كان المستخدم قد صوت مسبقًا
    if user_votes[user_id] == candidate_key:
        bot.answer_callback_query(call.id, "🚫 لقد قمت بالفعل بالتصويت لهذا المتسابق.", show_alert=True)
        return

    try:
        # إذا كان المستخدم قد صوت لشخص آخر
        if user_votes[user_id] is not None:
            previous_vote = user_votes[user_id]
            candidates[previous_vote]['votes'] -= 1

        # تسجيل التصويت الجديد
        # تسجيل التصويت الجديد
        candidates[candidate_key]['votes'] += 1
        user_votes[user_id] = candidate_key

        # تحديث رسالة التصويت بعد تسجيل الصوت
        update_vote_buttons(call.message.chat.id, call.message.message_id, candidate_key)

        bot.answer_callback_query(call.id, "✅ تم تسجيل تصويتك بنجاح!")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ حدث خطأ أثناء التصويت: {e}")

# التحقق من المستخدم
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if is_bot_or_fake(message.from_user):
        bot.send_message(message.chat.id, "🚫 لا يمكنك التصويت، حسابك غير مؤهل.")
        banned_users.add(user_id)
        return

    try:
        bot.send_message(message.chat.id, "🎉 أهلاً بك! يمكنك الآن التصويت للمتسابقين.")
        send_candidates_list(message.chat.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء تحميل المتسابقين: {e}")

# حظر المستخدمين الوهميين
@bot.message_handler(func=lambda message: message.from_user.id in banned_users)
def handle_banned_users(message):
    bot.send_message(message.chat.id, "🚫 حسابك محظور من استخدام هذا البوت.")

# إضافة try-except للأخطاء المحتملة
@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    try:
        bot.send_message(message.chat.id, "❌ لم أفهم طلبك. استخدم /start لعرض المتسابقين.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ: {e}")

# تشغيل البوت
bot.polling(none_stop=True)