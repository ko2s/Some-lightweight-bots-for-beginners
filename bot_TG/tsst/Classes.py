from info import *
from def_main import tset_next_massage,rest,masage_text_next,information
class Command_handln():
    def __init__(self):
        self.data = Database()
        self.bote = Bote()
        self.admin = Admin()
        self.group = Group()
    def user_info(self,message):
        self.user = message.from_user
        self.chat_id = self.user.id
        self.first_name = self.user.first_name or "بدون اسم اول"
        self.last_name = self.user.last_name or "بدون اسم ثاني"
        self.full_name = f"{self.first_name} {self.last_name}".strip()
        self.username = self.user.username or "بدون يوزر"
        self.language = self.user.language_code
        self.is_bot = self.user.is_bot
    def handle_user(self,message):
        self.user_info(message)
        __dete = self.data.readData(f"/users/{self.chat_id}")
        if __dete:
            if message.chat.type == "private":
                self.handle_existing_user(message, self.admin.admin_start(self.chat_id))
            elif message.chat.type in ["group","supergroup"]:
                self.group.manage_members(message)
    def send_welcome_message(self,chat_id, message):
        data = self.data.readData('/Welcome Message/')
        if start_text:
            text = self.edit_text_start(message, start_text[0], chat_id)
        elif data and "Message" in data:
            text = self.edit_text_start(message, data["Message"], chat_id)
            start_text.append(text)
        else:
            text = "مرحبًا بك في البوت!"

        bot.send_message(chat_id, text, parse_mode='Markdown')
    def edit_text_start(self,message,text,chat_id):
        if text:
            text_x = text.format(
                first_name = self.first_name,last_name = self.last_name,
                full_name = self.full_name,username = self.username,chat_id = chat_id,
                bot_first_name = self.bote.bot_first_name,bot_last_name = self.bote.bot_last_name,
                bot_full_name = self.bote.bot_full_name,bot_username = self.bote.bot_username,
                admin_last_name = self.admin.admin_last_name,admin_first_name = self.admin.admin_first_name,
                full_name_admin = self.admin.full_name_admin,admin_user = self.admin.admin_user,language = self.language,)
        return text_x
    def handle_existing_user(self, message, is_admin):
        if message.text.startswith('/start'):
            if is_admin:
                self.send_admin_panel(self.chat_id)
            else:
                self.send_welcome_message(self.chat_id, message)

        elif message.text.startswith('/id'):
            bot.reply_to(message, f"*YOUR ID* : `{self.chat_id}`", parse_mode='Markdown')

        elif message.text.startswith('/help'):
            bot.reply_to(message, "إذا كان هناك خطأ، الرجاء التواصل مع المطور: @ko_2s")
    def send_admin_panel(self,chat_id):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(
            KeyboardButton("اضافة ادمن"),
            KeyboardButton("حذف ادمن"),
            KeyboardButton("الإحصائية 📊"),
            KeyboardButton('اعدادات البوت')
        )
        bot.send_message(chat_id, f"مرحبا بك يا أدمن 🤍\n{self.full_name}\nاختر أحد الخيارات ليتم تنفيذها:", reply_markup=markup)  
class Student():
    pass
class Teacher():
    pass
class Bote():
    def __init__(self):
        self.botInfo()

    def botInfo(self):
        self.bot_info = bot.get_me()
        self.bot_username = self.bot_info.username
        self.bot_first_name = self.bot_info.first_name
        self.bot_last_name = self.bot_info.last_name
        self.bot_full_name = self.bot_info.full_name
    
class Group():
    def __init__(self):
        pass
    def manage_members(self,message: Message):
        try:
            if message.chat.type not in ["group", "supergroup"]:
                bot.reply_to(message, "هذا الأمر متاح فقط في المجموعات.")
                return

            if not message.reply_to_message:
                bot.reply_to(message, "يرجى الرد على رسالة العضو المراد تنفيذ الأمر عليه.")
                return

            user_id = message.reply_to_message.from_user.id
            chat_id = message.chat.id
            admin_id = message.from_user.id
            bot_id = bot.get_me().id

            # التحقق إذا كان الأمر موجهاً إلى البوت
            if user_id == bot_id and not message.text.startswith("/kick_bot"):
                bot.reply_to(message, "لا يمكن تنفيذ هذا الأمر على البوت.")
                return

            admin_status = bot.get_chat_member(chat_id, admin_id).status
            if admin_status not in ['administrator', 'creator']:
                bot.reply_to(message, "يجب أن تكون مشرفًا لاستخدام هذا الأمر.")
                return

            bot_status = bot.get_chat_member(chat_id, bot_id)
            if not bot_status.can_restrict_members:
                bot.reply_to(message, "ليس لدي صلاحيات كافية لتنفيذ هذا الأمر.")
                return

            # التحقق من نوع المجموعة (عامة أم خاصة)
            if bot.get_chat(chat_id).invite_link:
                group_type = "عامة"
            else:
                group_type = "خاصة"

            # تنفيذ الأوامر
            if message.text.startswith("/kick"):
                bot.kick_chat_member(chat_id, user_id)
                bot.reply_to(message, "تم طرد العضو بنجاح.")
            elif message.text.startswith("/ban"):
                bot.ban_chat_member(chat_id, user_id)
                bot.reply_to(message, "تم حظر العضو بنجاح.")
            elif message.text.startswith("/unban"):
                bot.unban_chat_member(chat_id, user_id)
                bot.reply_to(message, "تم رفع الحظر عن العضو بنجاح.")
            elif message.text.startswith("/mute"):
                bot.restrict_chat_member(chat_id, user_id, can_send_messages=False)
                bot.reply_to(message, "تم كتم العضو بنجاح.")
            elif message.text.startswith("/unmute"):
                bot.restrict_chat_member(chat_id, user_id, can_send_messages=True)
                bot.reply_to(message, "تم إلغاء الكتم عن العضو بنجاح.")
            elif message.text.startswith("/info"):
                member_info = bot.get_chat_member(chat_id, user_id)
                bot.reply_to(message, f"معلومات العضو:\nالاسم: {member_info.user.first_name}\nالمعرف: {member_info.user.id}\nالحالة: {member_info.status}")
            elif message.text.startswith("/warn"):
                warnings[user_id] = warnings.get(user_id, 0) + 1
                if warnings[user_id] >= 3:  # على سبيل المثال 3 تحذيرات
                    bot.kick_chat_member(chat_id, user_id)
                    bot.reply_to(message, "تم طرد العضو بسبب تجاوز حد التحذيرات.")
                    warnings[user_id] = 0
                else:
                    bot.reply_to(message, f"تم تحذير العضو. عدد التحذيرات: {warnings[user_id]}")
            elif message.text.startswith("/lock"):
                bot.set_chat_permissions(chat_id, ChatPermissions(can_send_messages=False))
                bot.reply_to(message, "تم قفل الدردشة.")
            elif message.text.startswith("/unlock"):
                bot.set_chat_permissions(chat_id, ChatPermissions(can_send_messages=True))
                bot.reply_to(message, "تم فتح الدردشة.")
            # elif message.text.startswith("/rules"):
            #     bot.reply_to(message, "قواعد المجموعة:\n1. الاحترام متبادل.\n2. ممنوع السبام.\n3. الالتزام بالمواضيع المحددة.")
            elif message.text.startswith("/kick_bot"):
                bot.leave_chat(chat_id)
        except Exception as e:
            logging.error(f"Error in manage_members: {e}")
            bot.reply_to(message, "حدث خطأ أثناء تنفيذ الأمر.")

class Database():
    def add_informution(self,path,info:dict):
        db.reference(path).set(info)
    def add_new_user(self,chat_id, full_name, username, language, is_bot):
        joining_data = rest(chat_id)
        info = {
            'full_name': full_name,
            'username': username,
            'language': language,
            "joining": joining_data,
            "is_Bot": is_bot,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.add_informution(f'/users/{chat_id}',info)
    def readData(self,path):
        return db.reference(path).get()
    def searchForUsername(self,username):
        data = self.readData("users")
        for userid in data:
            if data[userid]["username"] == "ko_2s":
                return userid
        return False

class Admin:
    def __init__(self):
        self.adminInfo()
        self.deta = Database()
    def adminInfo(self):
        self.admin_chate = bot.get_chat(admin[0]) #هذه الطريقة لي جلب معلومة معيننه من الادمن
        self.admin_last_name = self.admin_chate.last_name
        self.admin_first_name = self.admin_chate.first_name
        self.full_name_admin = f"{self.admin_first_name} {self.admin_last_name}" if self.admin_last_name else self.admin_first_name
        self.admin_user = self.admin_chate.username
    def admin_start(self, chat_id):
        """يتحقق مما إذا كان المستخدم أدمن أم لا"""
        date = self.deta.readData(f"/Aministrtor/{chat_id}")
        if date:
            return True
        return False
    def admin_add(self, message):
        """يضيف المستخدم إلى قائمة الأدمن إذا كان لديه رابط تيليجرام صالح أو يوزر أو ID"""
        chat_id = message.chat.id
        text = message.text.strip()
        if tset_next_massage(message):
            masage_text_next(message)
            return
        # تعريف أنماط الروابط، اليوزر (@username)، والـ ID (أرقام فقط)
        telegram_link_pattern = re.compile(r'(https?://t\.me/[^\s]+)')
        telegram_user_pattern = re.compile(r'^@[A-Za-z0-9_]+$')
        telegram_id_pattern = re.compile(r'^\d+$')
        ref = db.reference(f'/users')
        data = ref.get()
        # التحقق مما إذا كانت الرسالة تحتوي على رابط
        if telegram_link_pattern.search(text) or telegram_user_pattern.match(text):
            # التعامل مع الرابط
            # استخراج المستخدم من الرابط
            if telegram_link_pattern.search(text):
                user_info = text.split("/")[-1]
            else : user_info = text[1:]
            if self.admin_start(user_id):
                bot.send_message(chat_id,"عذراً، تم إضافة هذا الأدمن مسبقاً.")
                return
            else:
                user_id = self.deta.searchForUsername(user_info)
                if not user_id:
                    bot.send_message(chat_id,"عذراً، هذا ليس من ضمن مستخدمي البوت.")
                    return
                text , photo = information(user_id)
                if photo:
                    keyboard = telebot.types.InlineKeyboardMarkup()
                    keyboard.add(telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin'), telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin'))
                    رسالة = bot.send_photo(chat_id, photo, caption=text,reply_markup=keyboard)
                    user_chat_admin.append(user_id)
                    user_chat_admin.append(رسالة.message_id)
                    return
                elif not photo:
                    keyboard = telebot.types.InlineKeyboardMarkup()
                    btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                    btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                    keyboard.add(btn2, btn1)
                    رسالة = bot.send_message(chat_id,text=text,reply_markup=keyboard)
                    user_chat_admin.append(user_id)
                    user_chat_admin.append(رسالة.message_id)
                    return  
        elif telegram_id_pattern.match(text):
            # التعامل مع الـ ID
            user_info = int(text)
            if self.admin_start(user_info):
                bot.send_message(chat_id,"عذراً، تم إضافة هذا الأدمن مسبقاً.")
                return
            else:
                if not self.deta.readData(f"users/{user_info}"):
                    bot.send_message(chat_id,"عذراً، هذا ليس من ضمن مستخدمي البوت.")
                    return
                text , photo = information(user_info)
                try:
                    if photo:
                        keyboard = telebot.types.InlineKeyboardMarkup()
                        btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                        keyboard.add(btn2, btn1)
                        رسالة = bot.send_photo(chat_id, photo, caption=text,reply_markup=keyboard)
                        user_chat_admin.append(user_info)
                        user_chat_admin.append(رسالة.message_id)
                        return
                    elif photo == False:
                        keyboard = telebot.types.InlineKeyboardMarkup()
                        btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                        keyboard.add(btn2, btn1)
                        رسالة = bot.send_message(chat_id,text=text,reply_markup=keyboard)
                        user_chat_admin.append(user_info)
                        user_chat_admin.append(رسالة.message_id)
                except:
                    pass
        else:
            bot.send_message(chat_id, "يرجاء ارسال رابط صالح او يوزر صالح 🙂")