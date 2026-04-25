from info_bot import *


class Admin:
    def __init__(self, bot, admin_list):
        self.bot = bot
        self.admin_list = admin_list
        self.admin_list.clear()
        admin.append(developer)
        try:
            ref = db.reference(f'/Aministrtor')
            data = ref.get()
            for user in data:
                if int(user) == admin[0]:
                    continue
                else:
                    admin.append(user)
        except:
            examine(admin[0])
    def admin_start(self, message_chat):
        """يتحقق مما إذا كان المستخدم أدمن أم لا"""
        examine(admin[0])
        try:
            ref = db.reference(f'/Aministrtor')
            data = ref.get()
            for userad in data:
                if int(message_chat) == int(userad):
                    return True
            return False
        except:
            pass
        

    def admin_user(self, message):
        """يبحث عن معرف المستخدم إذا كان أدمن"""
        ref = db.reference(f'/Aministrtor')
        data = ref.get()
        for admin_us in data:
            if message == admin_us:
                return True
        
        return False

    def admin_add(self, message):
        """يضيف المستخدم إلى قائمة الأدمن إذا كان لديه رابط تيليجرام صالح أو يوزر أو ID"""
        chat_id = message.chat.id
        text = message.text.strip()
        tset = tset_next_massage(message)
        if tset == True:
            masage_text_next(message)
            return 
        # تعريف أنماط الروابط، اليوزر (@username)، والـ ID (أرقام فقط)
        telegram_link_pattern = re.compile(r'(https?://t\.me/[^\s]+)')
        telegram_user_pattern = re.compile(r'^@[A-Za-z0-9_]+$')
        telegram_id_pattern = re.compile(r'^\d+$')
        ref = db.reference(f'/users')
        data = ref.get()
        # التحقق مما إذا كانت الرسالة تحتوي على رابط
        if telegram_link_pattern.search(text):
            # التعامل مع الرابط
            #self.bot.send_message(chat_id, "تم التعرف على رابط تيليجرام.")
            # استخراج المستخدم من الرابط
            user_info = text.split("/")[-1]
            
            for user_id in data:
                ref = db.reference(f'/users/{user_id}')
                data = ref.get()
                
                for key,Value in data.items():
                    if Value == user_info:
                        tset = self.admin_user(user_id)
                        if tset == True:
                            bot.send_message(chat_id,"عذراً، تم إضافة هذا الأدمن مسبقاً.")
                            return
                        text , photo = information(user_id)
                        if photo:
                            keyboard = telebot.types.InlineKeyboardMarkup()
                            btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                            btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                            keyboard.add(btn2, btn1)
                            رسالة = bot.send_photo(chat_id, photo, caption=text,reply_markup=keyboard)
                            user_chat_admin.append(user_id)
                            user_chat_admin.append(رسالة.message_id)
                            return
                        elif photo == False:
                            keyboard = telebot.types.InlineKeyboardMarkup()
                            btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                            btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                            keyboard.add(btn2, btn1)
                            رسالة = bot.send_message(chat_id,text=text,reply_markup=keyboard)
                            user_chat_admin.append(user_id)
                            user_chat_admin.append(رسالة.message_id)
                            return
            bot.send_message(chat_id,"عذراً، هذا ليس من ضمن مستخدمي البوت.")
            return  
        
        elif telegram_user_pattern.match(text):
            # التعامل مع اليوزر
            #self.bot.send_message(chat_id, "تم التعرف على يوزر تيليجرام.")
            user_info = text[1:]
            # srach_user = bot.get_chat(user_info)
            for user_id in data:
                ref = db.reference(f'/users/{user_id}')
                data = ref.get()
                for key,Value in data.items():
                    if Value == user_info:
                        tset = self.admin_user(user_id)
                        if tset == True:
                            bot.send_message(chat_id,"عذراً، تم إضافة هذا الأدمن مسبقاً.")
                            return
                        text , photo = information(user_id)
                        if photo:
                            keyboard = telebot.types.InlineKeyboardMarkup()
                            btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                            btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                            keyboard.add(btn2, btn1)
                            رسالة = bot.send_photo(chat_id, photo, caption=text,reply_markup=keyboard)
                            user_chat_admin.append(user_id)
                            user_chat_admin.append(رسالة.message_id)
                            return
                        elif photo == False:
                                keyboard = telebot.types.InlineKeyboardMarkup()
                                btn1 = telebot.types.InlineKeyboardButton(text='📥 اضافة', callback_data='add_admin')
                                btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='No_add_admin')
                                keyboard.add(btn2, btn1)
                                رسالة = bot.send_message(chat_id,text=text,reply_markup=keyboard)
                                user_chat_admin.append(user_id)
                                user_chat_admin.append(رسالة.message_id)
                                return
            bot.send_message(chat_id,"عذراً، هذا ليس من ضمن مستخدمي البوت.") 
            return        

        # التحقق مما إذا كانت الرسالة تحتوي على ID (أرقام فقط)
        elif telegram_id_pattern.match(text):
            # التعامل مع الـ ID
            #self.bot.send_message(chat_id, "تم التعرف على ID تيليجرام.")
            user_info = int(text)  
            tset = self.admin_user(user_info)
            if tset == True:
                bot.send_message(chat_id,"عذراً، تم إضافة هذا الأدمن مسبقاً.")
                return
            else:
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
                    pass # bot.send_message(chat_id,"عذراً، هذا ليس من ضمن مستخدمي البوت.")    
        else:
            self.bot.send_message(chat_id, "لم يتم التعرف على رابط أو يوزر أو ID صالح.")
admin_chat = Admin(bot, admin)

def rest (chat_id):
    payload = json.dumps({"telegramId": chat_id})
    try:
        # إرسال الطلب إلى الخدمة الخارجية
        response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=payload)
        # التحقق من حالة الرد
        if response.status_code == 200:
            # قراءة البيانات بصيغة JSON
            data = response.json()
            # التحقق من وجود البيانات المطلوبة
            if 'data' in data and 'date' in data['data']:
                account_creation_date = data['data']['date']

                # صياغة الرد لعرض التاريخ
                return account_creation_date #تاريخ إنشاء حسابك على تليجرام هو:

    except requests.exceptions.RequestException as e:
        # معالجة الأخطاء المتعلقة بالشبكة أو الخدمة
        account_creation_date =  f"• حدث خطأ أثناء الاتصال بالخدمة الخارجية"

def SARCH_USER(chat_id):
    ref = db.reference(f'/users')
    data = ref.get()
    if data:
        for usered in data:
            if int(usered) == int(chat_id):
                return True
    return False


information_text = {
    "full_name": "الإسم",
    "username": "يوزر المستخدم",
    "joining": "تاريخ الانضمام",
    "language": "اللغة",
}


def information(user_id):
    try:
        ref = db.reference(f'/users/{user_id}')
        user_data = ref.get()

        if not user_data:
            return "لم يتم العثور على بيانات للمستخدم", False
        
        send = ""
        for key, value in user_data.items():
            if key == "created_at" or key == "is_Bot":
                continue

            if key == "language":
                if value == "ar":
                    value = "العربية 🇱🇾"
                elif value == "en":
                    value = "English 🇬🇧"

            elif key == "username":
                value = f'@{value}'

            send += f"{information_text.get(key, key)} : {value}\n"

        # جلب صورة المستخدم إن وجدت
        user_chat = bot.get_user_profile_photos(user_id)
        if user_chat.total_count > 0:
            file_id = user_chat.photos[0][-1].file_id
            return send, file_id
        else:
            return send, False

    except Exception as e:
        print(f"حدث خطأ: {e}")
        return "حدث خطأ أثناء جلب البيانات", False
def examine(user_id):
    ref = db.reference(f'/users/{user_id}')
    data = ref.get()
    for key,Value in data.items():
        keyls.append(key)
        Valuels.append(str(Value))
    ref = db.reference(f'/Aministrtor')
    data = ref.get()
    if  data is None:
        db.reference(f'/Aministrtor/{int(user_id)}').set({
                        keyls[1]: Valuels[1],
                        keyls[5]: Valuels[5],
                        keyls[4]: Valuels[4],
                        keyls[3]: Valuels[3],
                        keyls[0]: Valuels[0],
                        })
        keyls.clear() ; Valuels.clear()
def edit_text_start(message,text,chat_id):
    user = message.from_user
    first_name = user.first_name if user.first_name else "بدون اسم اول"
    last_name = user.last_name if user.last_name else "بدون اسم ثاني"
    full_name = f"{first_name} {last_name}" if last_name else first_name
    username = user.username if user.username else "بدون يوزر"
    bot_info = bot.get_me()
    bot_username = bot_info.username
    bot_first_name = bot_info.first_name
    bot_last_name = bot_info.last_name
    bot_full_name = bot_info.full_name
    admin_chate = bot.get_chat(admin[0]) #هذه الطريقة لي جلب معلومة معيننه من الادمن
    admin_last_name = admin_chate.last_name
    admin_first_name = admin_chate.first_name
    full_name_admin = f"{admin_first_name} {admin_last_name}" if admin_last_name else admin_first_name
    admin_user = admin_chate.username
    language = user.language_code
    if text:
        text_x = text.format(
            first_name = first_name,
            last_name = last_name,
            full_name = full_name,
            username = username,
            chat_id = chat_id,
            bot_first_name = bot_first_name,
            bot_last_name = bot_last_name,
            bot_full_name = bot_full_name,
            bot_username = bot_username,
            admin_last_name = admin_last_name,
            admin_first_name = admin_first_name,
            full_name_admin = full_name_admin,
            admin_user = admin_user,
            language = language,
            
        )
    return text_x
def text_start(message):
    user = message.from_user
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    text = f"""{text}"""
    chat_id = user.id
    text_x = edit_text_start(message,text,chat_id)
    start_text.append(text)
    db.reference(f'/Welcome Message/').set({
                 "Message" : text,
                'created_at': created_at
                })
    bot.send_message(chat_id,f"تم اضافة رسالة الترحيب بنجاح ✅\n شكل رسالة الترحيب التي تظهر للمستخدم\n {text_x}",parse_mode='Markdown')
  
def add_channel_or_user(user, chat_id):
    try:
        if user in channels:
            bot.send_message(chat_id, "عذرًا، تم إضافة هذه القناة مسبقًا ✅")
        else:
            channels.append(user)
            bot.send_message(chat_id, "تمت إضافة القناة بنجاح ✅")
    except Exception as e:
        bot.send_message(chat_id, f"حدث خطأ أثناء إضافة القناة: {str(e)}")

def handle_forward_or_text_message(message, chat_id):
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    try:
        if message.forward_from:
            # التعامل مع الرسالة المحولة من مستخدم
            user = message.forward_from
            first_name = user.first_name if user.first_name else "بدون اسم اول"
            last_name = user.last_name if user.last_name else "بدون اسم ثاني"
            user_info = f"User ID: `{user.id}`\nName: {first_name} {last_name}\nUsername: @{user.username if user.username else 'No username'}"
            bot.send_message(chat_id, f"تم تحويل الرسالة من مستخدم:\n{user_info}",parse_mode='Markdown')
            user = f"@{user.username if user.username else 'No username'}"
            add_channel_or_user(user, chat_id)

        elif message.forward_from_chat:
            # التعامل مع الرسالة المحولة من مجموعة أو قناة
            chat = message.forward_from_chat
            chat_info = f"Chat ID: `{chat.id}`\nChat Title: {chat.title}\nChat Type: {chat.type}\nUsername: @{chat.username if chat.username else 'No username'}"
            bot.send_message(chat_id, f"تم تحويل الرسالة من مجموعة أو قناة:\n{chat_info}",parse_mode='Markdown')
            user = f"@{chat.username if chat.username else 'No username'}"
            add_channel_or_user(user, chat_id)

        elif message.text:
            # التعامل مع الرسائل النصية
            try:
                if message.text.isdigit():
                    # إذا كانت الرسالة رقمية، تعامل معها كـID
                    chat = bot.get_chat(int(message.text))
                    chat_info = f"Chat ID: `{chat.id}`\nChat Title: {chat.title}\nChat Type: {chat.type}\nUsername: @{chat.username if chat.username else 'No username'}"
                    bot.send_message(chat_id, f"تم استلام ID القناة:\n{chat_info}",parse_mode='Markdown')
                    user = f"@{chat.username if chat.username else str(chat.id)}"  # استخدم الـID إذا لم يكن هناك اسم مستخدم
                
                else:
                    chat = bot.get_chat(message.text)
                
                chat_info = f"Chat ID: `{chat.id}`\nChat Title: {chat.title}\nChat Type: {chat.type}\nUsername: @{chat.username if chat.username else 'No username'}"
                bot.send_message(chat_id, f"تم استلام اسم المستخدم:\n{chat_info}",parse_mode='Markdown')
                
                user = f"@{chat.username if chat.username else message.text}"
                add_channel_or_user(user, chat_id)
            except Exception as e:
                bot.send_message(chat_id, f"حدث خطأ أثناء جلب معلومات القناة: {str(e)}")

    except Exception as e:
        bot.send_message(chat_id, f"حدث خطأ: {str(e)} ⛔️")

             
def send_subscription_message(chat_id):
    myMarkup = telebot.types.InlineKeyboardMarkup()
    for channel in channels:
        try:
            my_chat = bot.get_chat(channel)
            myMarkup.add(telebot.types.InlineKeyboardButton(text=my_chat.title, url=my_chat.invite_link))
        
        except Exception as e:
            print(f"Error getting chat info for {channel}: {e}")
    if len(channels)>1:
        bot.send_message(
            chat_id,
            "عزيزي، يجب عليك الاشتراك في جميع القنوات التالية لاستخدام البوت:",
            reply_markup=myMarkup
        )
    else:
        bot.send_message(
            chat_id,
            "عزيزي، يجب عليك الاشتراك في القناة التالية لاستخدام البوت:",
            reply_markup=myMarkup
        )    
def check_subscription(chat_id):
    for channel in channels:
        try:
            member_status = bot.get_chat_member(channel, chat_id).status
            if member_status in ['left', 'restricted', 'kicked']:
                return False
        except Exception as e:
            print(f"Error checking subscription for {chat_id} in {channel}: {e}")
            return False
    return True
def massege_Ass(message):
    masge_Ass = message.text
    chat_id = message.from_user.id
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    # استرجاع المرجع
    ref = db.reference(f'/reply/')
    data = ref.get()
    coun = 1
    # التحقق مما إذا كانت البيانات موجودة
    if data is None:
        reply_ms.append(masge_Ass) #0
        name = f'red : 1'
        rednmper.append(name)

        keyboard = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton(text='اضافة رد نص', callback_data='text_edd')
        btn2 = InlineKeyboardButton(text='اضافة رد ازرار', callback_data='boten_add')
        btn3 = InlineKeyboardButton("اضافة صورة",callback_data="photo_send_to")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3)
        mes1 = bot.send_message(message.from_user.id, "اختر احد الخيارات الاتيه : ",reply_markup=keyboard)
        return
    
    # التحقق من وجود الرسالة في قاعدة البيانات
    for red in data:
        ref = db.reference(f'/reply/{red}')
        red_data = ref.get()

        if red_data is None:
            continue
        
        for key in red_data:
            
            if masge_Ass == key:
                mes = bot.send_message(message.from_user.id, f"*عذراً، هذه الرسالة محفوظة مسبقاً، الرجاء إدخال رسالة أخرى أو اكتب أمر /stop\nالرسالة موجودة هنا: {red}*", parse_mode='Markdown')
                bot.register_next_step_handler(mes, massege_Ass)
                return
            elif key == "created_at":
                continue

    # إذا لم تكن الرسالة موجودة، طلب إدخال رد جديد
    reply_ms.append(masge_Ass) #0
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='اضافة رد نص', callback_data='text_edd')
    btn2 = telebot.types.InlineKeyboardButton(text='اضافة رد ازرار', callback_data='boten_add_1')
    btn3 = InlineKeyboardButton("اضافة صورة",callback_data="photo_send_to")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)
    mes1 = bot.send_message(message.from_user.id, "اختر احد الخيارات الاتيه : ",reply_markup=keyboard)
    for x in range(len(data)+coun):
        for red in data:
            if red == f'red : {coun}':
                coun += 1
                
            else:
                # إنشاء اسم جديد للرد
                name = f'red : {coun}'
                rednmper.append(name)#0
                return
    return


def massege_red(message):
    global reply_ms
    coun = 1
    reply_text = message.text  # تغيير الاسم لتجنب التعارض مع اسم الدالة
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    # استرجاع البيانات من Firebase
    ref = db.reference(f'/reply/')
    data = ref.get()

    # التحقق مما إذا كانت البيانات موجودة
    if data is None:
        name = f'red : {coun}'
        
        
        # إنشاء أزرار Inline Keyboard
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn_yes = telebot.types.InlineKeyboardButton(text='موفق ❤️', callback_data='ter')
        btn_no = telebot.types.InlineKeyboardButton(text='غير موفق ❌', callback_data='fos')
        keyboard.add(btn_yes, btn_no)
        
        # إرسال الرسالة مع الأزرار
        confirmation_message = bot.send_message(
            message.from_user.id,
            f"*هل انت موفق على رفع هذا:\nالرسالة:\n{reply_ms[0]}\nالرد:\n{reply_text}*",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
        
        # تحديث المتغيرات
        reply_ms.append(reply_text)  # الرد
        reply_ms.append(name)        # الاسم
        reply_ms.append(confirmation_message.message_id) 
        return
    
    # البحث في البيانات
    for x in range(len(data)+coun):
        for red in data:
            if red == f'red : {coun}':
                coun += 1
                print(red)
            else:
                # إنشاء اسم جديد للرد
                name = f'red : {coun}'
                
                
                # إنشاء أزرار Inline Keyboard
                keyboard = telebot.types.InlineKeyboardMarkup()
                btn_yes = telebot.types.InlineKeyboardButton(text='موفق ❤️', callback_data='ter')
                btn_no = telebot.types.InlineKeyboardButton(text='غير موفق ❌', callback_data='fos')
                keyboard.add(btn_yes, btn_no)
                
                # إرسال الرسالة مع الأزرار
                confirmation_message = bot.send_message(
                    message.from_user.id,
                    f"*هل انت موفق على رفع هذا:\nالرسالة:\n{reply_ms[0]}\nالرد:\n{reply_text}*",
                    reply_markup=keyboard,
                    parse_mode='Markdown'
                )
                
                # تحديث المتغيرات
                reply_ms.append(reply_text)  # الرد
                reply_ms.append(name)        # الاسم
                reply_ms.append(confirmation_message.message_id)  # تخزين message_id للرسالة
                
                return
def massge(text,message) :
    red = []
    key_keu.clear()
    try:
        ref = db.reference(f'/reply/')
        data = ref.get()
        photo_url.clear()
        for message1 in data:
            ref = db.reference(f'/reply/{message1}')
            message_data = ref.get()
            
            for key , Value in message_data.items():
                if text == key:
                    if Value.startswith("http"):
                        photo_url.append(Value)
                        photo_url.append(message1)
                    elif isinstance(Value, str):
                        # إذا كانت القيمة نصًا، إرسالها كرسالة
                        bot.send_message(message.from_user.id, f"*{Value}*", parse_mode='Markdown')
                        return      
            if len(photo_url)>1:        
                ref = db.reference(f'/reply/{photo_url[1]}')
                message_data = ref.get()
                for key,Value in message_data.items():
                    
                    if key =="boten":
                            pass
                    elif key == "caption":
                        bot.send_photo(message.chat.id,photo_url[0],caption= Value)
                        return
                bot.send_photo(message.chat.id,photo_url[0])
                return
        for message1 in data:
            ref = db.reference(f'/reply/{message1}')
            message_data = ref.get()        
            for key , Value in message_data.items():
                if text in key:
                
                    if Value.startswith("http"):
                        photo_url.append(Value)
                        photo_url.append(message1)
                        
                    elif isinstance(Value, str):
                        # إذا كانت القيمة نصًا، إرسالها كرسالة
                        bot.send_message(message.from_user.id, f"*{Value}*", parse_mode='Markdown')
                        return      
            if len(photo_url)>1:        
                ref = db.reference(f'/reply/{photo_url[1]}')
                message_data = ref.get()
                for key,Value in message_data.items():
                    
                    if key =="boten":
                            pass
                    elif key == "caption":
                        bot.send_photo(message.chat.id,photo_url[0],caption= Value)
                        return
                bot.send_photo(message.chat.id,photo_url[0])    
    except Exception as e :
         storage =  re.compile((r"https?://storage"))
         url = re.compile(r"https?://(www\.)?[\w\-]+(\.[\w\-]+)+(/[^\s]*)?")
         keyboard = InlineKeyboardMarkup()
         if "dict" in str(e):
            ref = db.reference(f'/reply/{message1}')
            data = ref.get()
            for x in data:
                if  not x == "created_at":
                    ref = db.reference(f'/reply/{message1}/{x}')
                    data1 = ref.get()
                    for sic in data1:
                        text = sic
                        ref = db.reference(f'/reply/{message1}/{x}/{sic}')
                        data2 = ref.get()
                        for key,value in dict(data2).items():
                            if storage.search(value):
                                keyboard.add(InlineKeyboardButton(text=key, callback_data=f'lockel_{key}'))
                            elif url.search(value):
                                keyboard.add(InlineKeyboardButton(text=key, url=f"{value}"))
                            else:
                                keyboard.add(InlineKeyboardButton(text=key, callback_data=f'lockel_{key}'))    
                        key_keu.append(dict(data2))    
            mas = bot.send_message(message.chat.id,f"{text}",reply_markup=keyboard)
            key_keu.append(mas.message_id)
                        
def prssan(message):
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    chat_id = message.chat.id
    ref = db.reference(f'/reply/')
    data = ref.get()
    
    try:
        text = str(text).split(":")
        text = f"{text[0]}: {int(text[1])}"
        
        for red in data:
            if red == text:
                ref = db.reference(f'/reply/{red}')
                ref.delete()
                bot.send_message(chat_id,"*تم حذف الرسالة بنجاح ✅*",parse_mode='Markdown')
                return
        bot.send_message(chat_id,"*عذرآ، هذه الكود غير صحيح او تم حذف هذه الرسالة بلفعل ❌*",parse_mode='Markdown')    

    except Exception as e :
        bot.send_message(chat_id,f"حدث خطاء {e}")
def tset_next_massage(message):
    text = message.text
    if text in [boten_key_name.get("add_user"), boten_key_name.get("delet_user"),
                boten_key_name.get("add_admin"), boten_key_name.get("delet_admin"),
                boten_key_name.get("view_vote"), boten_key_name.get("settings"),
                boten_key_name.get("add_button_key")]:
        return True
        
def masage_text_next(message):
    text = message.text
    chat_id = message.chat.id
    try:
        if text in [boten_key_name.get("add_user"), boten_key_name.get("delet_user"),
                    boten_key_name.get("add_admin"), boten_key_name.get("delet_admin"),
                    boten_key_name.get("view_vote"), boten_key_name.get("settings"),
                    boten_key_name.get("add_button_key")]:
            handle_all_messages1(message)
    except Exception as e :
        print(e)
def handle_all_messages1(message):
    chat_id = message.from_user.id
    text = message.text
    is_admin = admin_chat.admin_start(chat_id)
    if is_admin:
        if text == boten_key_name.get("add_user"):
            send_admin_panel(chat_id)
        elif text == boten_key_name.get("add_admin"):
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='عرض قائمة الادمن', callback_data='arad_admin')
            btn2 = InlineKeyboardButton(text='اضافة ادمن', callback_data='add_next_admin')
            keyboard.add(btn1)
            keyboard.add(btn2)
            bot.send_message(chat_id,"اختر احد من الخيارات الاتيه",reply_markup=keyboard)
        
        elif text == boten_key_name.get("view_vote"):
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text="عرض عداد تصويت لي متسابق معين", callback_data='viewa_tsoey')
            btn2 = InlineKeyboardButton(text="الإحصائيات الكاملة", callback_data='stetes')
            btn3 = InlineKeyboardButton(text="من هو الفائز؟", callback_data='man_hoa')
            btn4 = InlineKeyboardButton(text="إجمالي عدد مستخدمي البوت", callback_data='usere_adda')
            btn5 = InlineKeyboardButton(text='كم مزال ع المسابقة؟', callback_data='tiemard')
            bt6 = InlineKeyboardButton(text = 'الساعة 🕘',callback_data="tameas")
            keyboard.add(btn1)
            keyboard.add(btn2)
            keyboard.add(btn3)
            keyboard.add(btn4)
            keyboard.add(btn5)
            keyboard.add(bt6)
            bot.send_message(chat_id,"اختر احد الخيارات الاتيه : ",reply_markup=keyboard)
        elif text == boten_key_name.get("settings"):
            markup_key.clear()
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='رسالة الترحيب', callback_data='wolcam')
            btn2 = InlineKeyboardButton(text='الاشتراك الاجباري', callback_data='chanl')
            btn3 = InlineKeyboardButton(text='اذاعة 📢', callback_data='user_all')
            btn4 = InlineKeyboardButton(text='الردود 📥', callback_data='reply')     
            btn5 = InlineKeyboardButton(text='اعدادات المحادثات ⚙️', callback_data='setting')
            btn6 = InlineKeyboardButton(text='المزيد من الاعدادات ⚙️', callback_data='setting_to')
            keyboard.add(btn1)
            keyboard.add(btn2)
            keyboard.add(btn3)
            keyboard.add(btn4)
            keyboard.add(btn5)
            keyboard.add(btn6)
            bot.send_message(chat_id,"اختر احد الخيارات الاتيه : ",reply_markup=keyboard)
            markup_key.append(keyboard)
        elif text == boten_key_name.get("delet_user"):
            ref = db.reference(f'/User_data/')
            data = ref.get()
            markup = InlineKeyboardMarkup()
            if data is None:
                bot.send_message(chat_id=chat_id, text="لا يوجد شىء متسابقين ⛔️")
                return
            for sec in data:
                markup.add(InlineKeyboardButton(f"{sec}" , callback_data= f"deletusrr_{sec}"))
            bot.send_message(chat_id,"اختر القسم الذي يوجد فيه المستخدم:",reply_markup= markup)
            markup_key1.append(markup)
        elif text == boten_key_name.get("delet_admin"):
            if chat_id != admin[0] and chat_id not in admin_stretor:
                
                bot.send_message(chat_id,"عذرآ، لا يمكنك حذف اي ادمن لان ليس لديك الصلاحيات الكافيه وحده المطور الاساسي هو من لديه هذه الصلاحية.")
            else:
                if chat_id in admin_stretor:
                    keyboard = InlineKeyboardMarkup()
                    btn1 = InlineKeyboardButton(text='عرض قائمة الادمن', callback_data='arad_admin')
                    btn2 = InlineKeyboardButton(text='حذف الادمن', callback_data='delet_admin')
                    keyboard.add(btn1)
                    keyboard.add(btn2)
                    bot.send_message(chat_id,"اختر احد من الخيارات الاتيه",reply_markup=keyboard)
                else:
                    if chat_id == admin[0]:
                        keyboard = InlineKeyboardMarkup()
                        btn1 = InlineKeyboardButton(text='اضافة مطور', callback_data='add_mtor')
                        btn2 = InlineKeyboardButton(text='حذف المطور', callback_data='delet_mtor')
                        btn3 = InlineKeyboardButton(text='عرض قائمة الادمن', callback_data='arad_admin')
                        btn4 = InlineKeyboardButton(text='حذف الادمن', callback_data='delet_admin')
                        keyboard.add(btn3)
                        keyboard.add(btn4)
                        keyboard.add(btn1)
                        keyboard.add(btn2)
                        bot.send_message(chat_id,"اختر احد من الخيارات الاتيه",reply_markup=keyboard)
                        return
                    keyboard = InlineKeyboardMarkup()
                    btn1 = InlineKeyboardButton(text='اضافة مطور', callback_data='add_mtor')
                    btn3 = InlineKeyboardButton(text='عرض قائمة الادمن', callback_data='arad_admin')
                    btn4 = InlineKeyboardButton(text='حذف الادمن', callback_data='delet_admin')
                    
                    keyboard.add(btn3)
                    keyboard.add(btn4)
                    keyboard.add(btn1)
                    bot.send_message(chat_id,"اختر احد من الخيارات الاتيه",reply_markup=keyboard)
            
        elif text == boten_key_name.get("add_button_key"):
            if candidates:
                bot.send_message(chat_id, "المسابقة قيد التشغيل ✅")
                return
            
            t1 = time.time()
            ref = db.reference(f'/User_data/')
            data = ref.get()
            candidates.clear()
            user_votes.clear()
            
            if data is None:
                bot.send_message(chat_id, "لا يوجد متسابقين ⛔️")
                return
            
            # معالجة المتسابقين
            for mtsabk in data:
                ref = db.reference(f'/User_data/{mtsabk}')
                data_us = ref.get()
                
                for sec in data_us:
                    ref = db.reference(f'/User_data/{mtsabk}/{sec}')
                    data_a = ref.get()
                    
                    for key, value in dict(data_a).items():
                        if key == "Name":
                            candidates[value] = {"name": value, "votes": 0, "section": mtsabk}
                            candidate_name = value
                            candidate_name_key.append(candidate_name)
            
            # إنشاء لوحة الأزرار العادية
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button1 = KeyboardButton(boten_key_name.get("add_user"))
            button2 = KeyboardButton(boten_key_name.get("add_admin"))
            button3 = KeyboardButton(boten_key_name.get("view_vote"))
            button4 = KeyboardButton(boten_key_name.get("settings"))
            button5 = KeyboardButton(boten_key_name.get("delet_user"))
            button6 = KeyboardButton(boten_key_name.get("delet_admin"))
            button7 = KeyboardButton(boten_key_name.get("stop_key"))
            
            markup.add(button1, button2)
            markup.add(button3, button4)
            markup.add(button5, button6)
            markup.add(button7)
            
            tss = time.time() - t1
            tss = round(tss, 2)
            
            bot.send_message(chat_id, f"*الزمن المستغرق للبدء بالثواني: {tss} ثانية*", parse_mode='Markdown', reply_markup=markup)
            
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton(text="اضافة وقت", callback_data="add_tim"),
                        InlineKeyboardButton(text="لا", callback_data="no_tim"))

            bot.send_message(chat_id, 
                            "🎉 تم بدء المسابقة! يمكن للمستخدمين الآن التصويت\nهل تريد اضافة زمن معين لانتهاء المسابقة", 
                            reply_markup=keyboard)
            
        elif text == boten_key_name.get("stop_key"):
            if  not candidates:
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                # إنشاء الأزرار
                button1 = KeyboardButton(boten_key_name.get("add_user"))
                button2 = KeyboardButton(boten_key_name.get("add_admin"))
                button3 = KeyboardButton(boten_key_name.get("view_vote"))
                button4 = KeyboardButton(boten_key_name.get("settings"))
                button5 = KeyboardButton(boten_key_name.get("delet_user"))
                button6 = KeyboardButton(boten_key_name.get("delet_admin"))
                button7 = KeyboardButton(boten_key_name.get("add_button_key"))
                markup.add(button1, button2)
                markup.add(button3, button4)
                markup.add(button5,button6)
                markup.add(button7)
                bot.send_message(chat_id,"لا توجد مسابقة قيد التشغيل ✅",reply_markup= markup)
                return
            if candidates:
                for x in user_votes.keys():
                    delete_old_messages(x)
                    if x not in admin:
                        bot.send_message(x,"لقد انتهت المسابقة، وسيتم الإعلان عن الفائز قريبًا.🕑")
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                # إنشاء الأزرار
                button1 = KeyboardButton(boten_key_name.get("add_user"))
                button2 = KeyboardButton(boten_key_name.get("add_admin"))
                button3 = KeyboardButton(boten_key_name.get("view_vote"))
                button4 = KeyboardButton(boten_key_name.get("settings"))
                button5 = KeyboardButton(boten_key_name.get("delet_user"))
                button6 = KeyboardButton(boten_key_name.get("delet_admin"))
                button7 = KeyboardButton(boten_key_name.get("add_button_key"))
                markup.add(button1, button2)
                markup.add(button3, button4)
                markup.add(button5,button6)
                markup.add(button7)
                for chat_admin in admin:
                    if chat_id == chat_admin:
                        bot.send_message(chat_admin,"تم إيقاف المسابقة وفقًا لطلبك ✅",reply_markup=markup)
                candidates1.clear()
                user_votes2.clear()
                candidates1.update(candidates)
                user_votes2.update(user_votes)
                user_votes.clear()
                candidates.clear()

        else:
            if text == message.text:
                massge(text,message)
            else:
                if text in message.text:
                    massge(text,message)      
    else:
        if text == message.text:
                massge(text,message)
        else:
            if text in message.text:
                massge(text,message)     
def add_section(message):
    text = message.text
    chat_id = message.chat.id
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_yes = telebot.types.InlineKeyboardButton(text='موفق ❤️', callback_data='tery')
    btn_no = telebot.types.InlineKeyboardButton(text='غير موفق ❌', callback_data='fosy')
    keyboard.add(btn_yes, btn_no)
    
    # إرسال الرسالة مع الأزرار
    bot.send_message(
        message.from_user.id,
        f"*هل انت موفق على رفع هذا القسم {text}*",
        reply_markup=keyboard,
        parse_mode='Markdown'
    )
    kasamem.append(text)
class User:
    def __init__(self, bot, user_list):
        self.bot = bot
        self.admin_list = user_list
    def add_user(self,message):
        coun = 0
        user_list.clear()
        self.text = message.text
        self.chat_id = message.chat.id
        ref = db.reference(f'/section/')
        data_usu = ref.get()
        tset = tset_next_massage(message)
        if tset == True:
            masage_text_next(message)
            return
        user_list.append(self.text)
        if data_usu is None:
            bot.send_message(self.chat_id,"عذرًا، لا يوجد قسم. الرجاء إضافة قسم ثم قم بإضافة متسابق.⛔️")
            return
        else:
            if not section:
                for x in data_usu:
                    section.append(x)
                KeyButton = InlineKeyboardMarkup()
                for sec in section:
                    KeyButton.add(InlineKeyboardButton(text = sec, callback_data=f"sec_{sec}"))
                    coun+=1
                bot.send_message(self.chat_id,"اخنر قسم من الاقسام الاتيه 🗂",reply_markup=KeyButton)
            else:
                KeyButton = InlineKeyboardMarkup()
                for sec in section:
                    KeyButton.add(InlineKeyboardButton(text = sec, callback_data=f"sec_{sec}"))
                    coun+=1
                bot.send_message(self.chat_id,"اخنر قسم من الاقسام الاتيه 🗂",reply_markup=KeyButton)   
def process_message(text):
    contains_text = any(not char in emoji.EMOJI_DATA for char in text)
    
    if contains_text:
        return False  
    emoji_list1.clear()
    emoji_list.append(text)
    emoji_list1.append(text)
    return True

def tset_emoje(message):
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if process_message(text):
        bot.reply_to(message, f"تم حفظ الإيموجي الخاص بك! {emoji_list1[0]}")
    else:
        bot.reply_to(message, "عذراً، الرجاء إرسال إيموجي فقط ⛔️")

def user_sarch(message):
    text = message.text
    user_id = message.chat.id
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    ref = db.reference(f'/users/')
    data = ref.get()
    if text:
        try:
            if not text.startswith("@") and not text.isdigit():
                bot.send_message(user_id,"عذرا، الرجاء اضافة علامة @ قبل اليوزر✅")
                return
            if text.startswith("@"):
                for us in data:
                    info = bot.get_chat(us)
                    user_name = info.username
                    if f"@{user_name}" == text:
                        chat_id = us
                        chat = bot.get_chat(chat_id)
                        first_name = chat.first_name if chat.first_name else "بدون اسم اول"
                        last_name = chat.last_name if chat.last_name else "بدون اسم ثاني"
                        full_name = f"{first_name} {last_name}" if last_name else first_name
                        username = chat.username if chat.username else "بدون يوزر"
                        massage = f"""اسم المستخدم : {full_name}
*Id المستخدم :* `{chat_id}`*
يوزره : @{username}
bio : {chat.bio if chat.bio else "بدون بايو"}
رابط حسابه : https://t.me/{username}*
"""
                        bot.send_message(user_id,f"{massage}",parse_mode='Markdown')
                        return
                return bot.send_message(user_id,"عذرًا، لم أجد المستخدم. المستخدم ليس مشترك في البوت.")
            elif text.isdigit():
                for x in data:
                    if text == x:
                        chat_id = x
                        chat = bot.get_chat(chat_id)
                        first_name = chat.first_name if chat.first_name else "بدون اسم اول"
                        last_name = chat.last_name if chat.last_name else "بدون اسم ثاني"
                        full_name = f"{first_name} {last_name}" if last_name else first_name
                        username = chat.username if chat.username else "بدون يوزر"
                        massage = f"""اسم المستخدم : {full_name}
*Id المستخدم :* `{chat_id}`
*يوزره : @{username}**
bio : {chat.bio if chat.bio else "بدون بايو"}
رابط حسابه : https://t.me/{username}*
"""
                        bot.send_message(user_id,f"{massage}",parse_mode='Markdown')
                        return
                return bot.send_message(user_id,"عذرًا، لم أجد المستخدم. المستخدم ليس مشترك في البوت.")
        except Exception as e:
            bot.send_message(admin[0],f"هناك خطاء في البحث عن مستخدم عن طريق ID\nالخطاء :{e}")
user_messages = defaultdict(list)

# عند التصويت يتم تحديث الرسائل
def update_vote(candidate_key):
    if candidate_key in candidates:
        # زيادة عدد الأصوات
        candidates[candidate_key]['votes'] += 1
        
        # تحديث الرسائل لجميع المستخدمين
        update_all_messages(candidate_key)
    else:
        print(f"المتسابق {candidate_key} غير موجود.")

def update_all_messages(candidate_key):
    if candidate_key in user_messages:
        
        for chat_id, message_id in user_messages[candidate_key]:
            try:
                update_vote_buttons(chat_id, message_id, candidate_key)
                print(f"تم تحديث الرسالة الخاصة بالمتسابق {candidate_key} للمحادثة {chat_id} والرسالة {message_id}")
            except telebot.apihelper.ApiException as api_error:
                error_description = str(api_error)
                if "message is not modified" in error_description:
                    print(f"الرسالة {message_id} لم تتغير.")
                elif "message to edit not found" in error_description:
                    print(f"الرسالة {message_id} غير موجودة، ربما تم حذفها.")
                    # إزالة الرسالة من القائمة إذا كانت غير موجودة
                    user_messages[candidate_key].remove((chat_id, message_id))
                elif "user is deactivated" in error_description or "bot was blocked" in error_description:
                    print(f"المستخدم قد حظر البوت أو الحساب معطل لرسالة {message_id}")
                else:
                    print(f"خطأ غير معروف مع الرسالة {message_id}: {error_description}")
            except Exception as e:
                print(f"Error in update_all_messages: {e}")
def is_bot_or_fake(user):
    if user.is_bot:
        return True
def fake_user(user):
    user_photos = bot.get_user_profile_photos(user.id)
    
    
    joining_data = rest(user.id)
    joining_month= str(joining_data).split("-")[1]
    joining_year= str(joining_data).split("-")[0]
    current_date = datetime.now(pytz.utc)
    current_year = current_date.year
    current_month = current_date.month
    if user.id in user_captcha_okke:
            return False
    if user_photos.total_count == 0:
        return True
    if user.language_code != 'ar':
        return True
    
    if current_year == int(joining_year) and current_month == int(joining_month):
        return True

    return False
    
    
# تعديل زر التصويت لكل رسالة معينة
def update_vote_buttons(chat_id, message_id, candidate_key):
    try:
        candidate = candidates[candidate_key]
        markup = InlineKeyboardMarkup()
        vote_button = InlineKeyboardButton(f"{vote_icon[0]} {candidate['votes']}", callback_data=f"vote_{candidate_key}")
        markup.add(vote_button)
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)
    except Exception as e:
        print(f"Error in update_vote_buttons: {e}")

# إرسال قائمة المرشحين للمستخدمين وتخزين معرف الرسالة
def send_candidates_list(chat_id):
    if not candidates:
        return

    # إذا كان لدى المستخدم رسائل قديمة، نقوم بحذفها
    if chat_id in user_messages and len(user_messages[chat_id]) > 0:
        delete_old_messages(chat_id)

    user_messages[chat_id] = []  # إعادة تعيين قائمة الرسائل للمستخدم

    for candidate_name, candidate_data in candidates.items():
        try:
            markup = InlineKeyboardMarkup()
            vote_button = InlineKeyboardButton(f"{vote_icon[0]} {candidate_data['votes']}", callback_data=f"vote_{candidate_name}")
            markup.add(vote_button)

            mass_text = """ملاحظة: يمكنك التصويت لي مرة واحدة فقط، ولا يمكنك التصويت لي من أكثر من مستخدم في نفس الوقت. إذا قمت بالتصويت لي عن طريق الخطأ، يمكنك التواصل مع مطور البوت لسحب تصويتك لمرة واحدة فقط."""
            mse = bot.send_message(chat_id, f"📛 <b>{candidate_name}</b>\n{mass_text}\n🔰 القسم: {candidate_data['section']}\n🗳 عدد الأصوات: {candidate_data['votes']}", parse_mode="HTML", reply_markup=markup)
            
            # تخزين معرف الرسالة في القائمة المخصصة للمستخدم
            user_messages[chat_id].append(mse.message_id)
            message_msid.append(mse.message_id)
        except Exception as e:
            print(f"Error in send_candidates_list: {e}")


def delete_old_messages(chat_id):
    """
    دالة لحذف الرسائل القديمة الخاصة بمستخدم معين
    """
    try:
        for message_id in user_messages.get(chat_id, []):
            try:
                bot.delete_message(chat_id, message_id)
            except telebot.apihelper.ApiTelegramException as e:
                pass

        # إعادة تعيين قائمة الرسائل بعد الحذف
        user_messages[chat_id] = []

    except Exception as e:
        pass
def generate_captcha():
    # إعداد النص العشوائي (4 أحرف)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    # إعداد الصورة
    img = Image.new('RGB', (100, 40), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # إعداد الخط (يمكنك استخدام مسار لملف خط معين لو أردت)
    font = ImageFont.load_default()

    # إضافة النص للصورة
    d.text((10, 10), captcha_text, font=font, fill=(0, 0, 0))

    # حفظ الصورة
    img_path = 'captcha.png'
    img.save(img_path)

    return captcha_text, img_path
def check_captcha(message):
    user_id = message.from_user.id
    if user_id in user_captcha_okke:
        return
    if user_captcha:
        
        # التحقق مما إذا كان المستخدم قد قام بإدخال النص الصحيح
        if message.chat.id in user_captcha and message.text == user_captcha[message.chat.id]:
            bot.reply_to(message, "تم التحقق من أنك إنسان! الآن يمكنك استخدام البوت.✅")
            # حذف النص بعد النجاح
            del user_captcha[message.chat.id]
            user_captcha_okke[user_id] = user_id
            os.remove("captcha.png")
        else:
            bot.reply_to(message, "خطأ ❌، الرجاء إعادة المحاولة.")
            # إعادة إرسال CAPTCHA في حال الفشل
            captcha_text, img_path = generate_captcha()
            user_captcha[message.chat.id] = captcha_text
            with open(img_path, 'rb') as img:
                bot.send_photo(message.chat.id, img, caption="يرجى المحاولة مرة أخرى:")
def boten_red(message):
    text = message.text
    chat_id = message.chat.id
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='يرسل صورة', callback_data='photo_send')
    btn2 = InlineKeyboardButton(text='يحول الي رابط', callback_data='url_send')
    btn3 = InlineKeyboardButton(text = "يرسل نص", callback_data="text_send")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)
    Button.append(text)#0
    bot.send_message(chat_id=chat_id,text = "اذا ضغط على الزر ماذا يفعل",reply_markup=keyboard)
def photo_send(message):
    photo = message.photo
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    url = re.compile(r"https?://(www\.)?[\w\-]+(\.[\w\-]+)+(/[^\s]*)?")
    if photo:
        # الحصول على أعلى دقة للصورة (آخر عنصر في القائمة)
        file_info = bot.get_file(photo[-1].file_id)
        
        # تحديد مسار حفظ الصورة
        downloaded_file = bot.download_file(file_info.file_path)
        current_time = datetime.now().strftime("%Y-%m-%d ; %H : %M")
        rando = f"{current_time}_{uuid.uuid4()}.png"
        file_name = f"boten {rando}"  # تخصيص اسم للصورة
        print(created_at)
        save_path = os.path.join(os.getcwd(), file_name)  # مسار الحفظ في المجلد الحالي
        
        # كتابة الصورة في الملف المحلي
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        upload_image(message,file_name)
    elif url.search(text):
        
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='اضافة ✅', callback_data='save')
            btn3 = InlineKeyboardButton(text = "لا", callback_data="no_save_no")
            keyboard.add(btn1)
            keyboard.add(btn3)
            bot.send_message(message.chat.id,"هل تريد اضافة الرابط للزر؟",reply_markup=keyboard)
            text_boten.append(text)
    else:
        keyboard = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton(text='اضافة ✅', callback_data='save')
        btn3 = InlineKeyboardButton(text = "لا", callback_data="no_save_no")
        keyboard.add(btn1)
        keyboard.add(btn3)
        bot.send_message(message.chat.id,"هل تريد اضافة النص للزر؟",reply_markup=keyboard)
        text_boten.append(text)
def photo_send_to(message):
    photo = message.photo
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if photo:
        # الحصول على أعلى دقة للصورة (آخر عنصر في القائمة)
        file_info = bot.get_file(photo[-1].file_id)
        
        # تحديد مسار حفظ الصورة
        downloaded_file = bot.download_file(file_info.file_path)
        current_time = datetime.now().strftime("%Y-%m-%d ; %H : %M")
        rando = f"{current_time}_{uuid.uuid4()}.png"

        file_name = rando  # تخصيص اسم للصورة
        
        save_path = os.path.join(os.getcwd(), file_name)  # مسار الحفظ في المجلد الحالي
        
        # كتابة الصورة في الملف المحلي
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        tes = upload_image2(file_name)   
        if tes:
            keyboard = telebot.types.InlineKeyboardMarkup()
            btn1 = telebot.types.InlineKeyboardButton(text='نعم', callback_data='photo_yas')
            btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='photo_no')
            keyboard.add(btn1, btn2)
            mes1 = bot.send_message(message.from_user.id, "هل تريد اضافة واصف للصورة",reply_markup=keyboard)
            return
    else:
        mes1 = bot.send_message(message.chat.id, "عذرا، الرجاء ارسال صورة مرات اخره :")
        bot.register_next_step_handler(mes1, photo_send)
def upload_image2(file_name):
    """
    تحميل صورة من المسار المحلي إلى Firebase Storage باستخدام اسم الصورة الموجود في متغير blob_name.
    """
    local_file_path = os.path.join(os.getcwd(), file_name)
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    
    try:
        blob.upload_from_filename(local_file_path)
        blob.make_public()
        # print(f"File '{local_file_path}' uploaded as '{file_name}'.")
        reply_ms.append(blob.public_url)#2
        # print(f"Public URL: {blob.public_url}")
        name = str(file_name).split(":")[0]
        os.remove(name)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
    return False    

def upload_image(message,blob_name):
    """
    تحميل صورة من المسار المحلي إلى Firebase Storage باستخدام اسم الصورة الموجود في متغير blob_name.
    """
    # استخدام اسم الصورة الموجود في blob_name
    current_image_name = blob_name
    
    # تحديد المسار المحلي للصورة التي ترغب في رفعها
    local_file_path = os.path.join(os.getcwd(), current_image_name)
    
    # رفع الصورة باستخدام blob_name كاسم الصورة في Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(blob_name)
    
    try:
        blob.upload_from_filename(local_file_path)
        blob.make_public()
        # print(f"File '{local_file_path}' uploaded as '{blob_name}'.")
        # print(f"Public URL: {blob.public_url}")
        keyboard = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton(text='حفظ ✅', callback_data='save')
        btn3 = InlineKeyboardButton(text = "لا", callback_data="no_save")
        keyboard.add(btn1)
        keyboard.add(btn3)
        chat_ida.append(message.chat.id)
        text_boten.append(blob.public_url)#0
        bot.send_message(message.chat.id, f"تم حفظ الصورة بنجاح [هنا]({blob.public_url})",parse_mode='Markdown',reply_markup= keyboard)
        name = str(blob_name).split(":")[0]
        os.remove(name)
        مسار_الصورة.append(blob_name)
    except Exception as e:
        bot.send_message(message.chat.id, f"لم يتم حفظ صورة.\n{e}")
def photo_yas(message):
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if text:
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='رفع الصورة والوصف', callback_data='photo_up')
        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_photo_up')
        keyboard.add(btn1, btn2)
        reply_ms.append(text) #3
        print(reply_ms)
        bot.send_photo(message.chat.id,reply_ms[2],caption=text,reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id,"الرجاء اضافة نص صالح!!")
def message_ass_as(message):
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if text:
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='موفق ✅', callback_data='boten_add')
        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_boten1')
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id,f"هل انت موفق على اضافة هذا النص؟\n{text}",reply_markup=keyboard)
        ts = True
        message_ass1.append(text)
        return ts
def delete_image(blob_name):
    bucket = storage.bucket()
    blob = bucket.blob(blob_name)

    try:
        blob.delete()
        print(f"تم حذف الصورة: {blob_name}")
    except Exception as e:
        print(f"حدث خطأ أثناء حذف الصورة: {str(e)}")  
def generate_qr(message):
    qr_text = message.text.strip()
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
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
def solve_expression(message):
    expression = message.text.strip()
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    try:
        # استخدام sympy لحل المعادلة
        result = sympify(expression)
        bot.send_message(message.chat.id, f"✅ الحل هو: {result}")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ حدث خطأ أثناء محاولة حل المسألة. تأكد من أنك كتبتها بشكل صحيح.")
def fetch_html(message):
    url = message.text.strip()
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
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
def file_format_markup():
    markup = types.InlineKeyboardMarkup()
    txt_button = types.InlineKeyboardButton(".txt", callback_data='create_txt')
    py_button = types.InlineKeyboardButton(".py", callback_data='create_py')
    env_button = types.InlineKeyboardButton(".env", callback_data='create_env')
    bat1 = InlineKeyboardButton(".html",callback_data="create_html")
    markup.add(txt_button, py_button, env_button)
    markup.add(InlineKeyboardButton(".html",callback_data="create_html"),InlineKeyboardButton(".css",callback_data="create_css"),InlineKeyboardButton(".javascript",callback_data="create_javascript"))
    if fldars:
        for i in fldars:
            markup.add(InlineKeyboardButton(f".{i}",callback_data=f"create_{i}"))
    markup.add(InlineKeyboardButton("اضافة نوع ملف اخر",callback_data="creas"))        
    return markup
def save_file(message, file_format):
    content = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    file_name = f"file.{file_format}"

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)

        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(file_name)
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء حفظ الملف: {str(e)}")

def fldar(message):
    text = message.text
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if text:
        if "." in text:
            tst = (str(text).split("."))[1]
            bot.send_message(message.chat.id, f"تم اضافة الملف بنجاح : ✅")
            fldars.append(tst)
        else:
            bot.send_message(message.chat.id, f"تم اضافة الملف بنجاح : ✅")
            fldars.append(text)
def handle_report(message):
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if message.text:
        bot.send_message(admin[0], f"🛠️ تم الإبلاغ عن مشكلة من @{message.from_user.username}:\n\n{message.text}")
        bot.send_message(message.chat.id, "✅ تم إرسال مشكلتك بنجاح! سيتواصل معك المطور قريبًا.")
    else:
        bot.send_message(message.chat.id, "❌ لم يتم تلقي أي نص. يرجى إرسال المشكلة مرة أخرى.")
def handle_suggestion(message):
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    if message.text:
        bot.send_message(admin[0], f"💡 اقتراح من @{message.from_user.username}:\n\n{message.text}")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك بنجاح للمطور!")
    elif message.photo:
        photo_id = message.photo[-1].file_id  # الحصول على أكبر صورة
        bot.send_photo(admin[0], photo_id, caption=f"💡 اقتراح من @{message.from_user.username} (صورة)")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك كصورة للمطور!")
    elif message.document:
        file_id = message.document.file_id
        bot.send_document(admin[0], file_id, caption=f"💡 اقتراح من @{message.from_user.username} (ملف)")
        bot.send_message(message.chat.id, "✅ تم إرسال اقتراحك كملف للمطور!")
    else:
        bot.send_message(message.chat.id, "❌ لم يتم تلقي أي محتوى. يرجى إرسال الاقتراح مرة أخرى.")

def get_arabic_am_pm(hour):
    if hour < 12:
        return "صباحاً"
    else:
        return "مساءً"

# دالة لإظهار وقت انتهاء المسابقة وبدء العد التنازلي
def start_competition(chat_id, duration_seconds,call):
    global end_time
    # تحديد وقت بدء المسابقة بتوقيت ليبيا
    start_time = datetime.now(pytz.utc).astimezone(libya_timezone)
    
    # تحديد وقت انتهاء المسابقة
    end_time = start_time + timedelta(seconds=duration_seconds)

    # تنسيق وقت الانتهاء بتوقيت ليبيا بتنسيق 12 ساعة مع AM/PM باللغة العربية
    end_time_str = end_time.strftime('%I:%M:%S')
    am_pm = get_arabic_am_pm(end_time.hour)

    # إرسال رسالة البداية مع العد التنازلي
    initial_text = (
        f"🎉 المسابقة بدأت الآن! 🎉\n"
        f"⏰ ستنتهي المسابقة في {end_time_str} {am_pm} بتوقيت ليبيا.\n"
        f"🕒 الوقت المتبقي: {duration_seconds // 60} دقيقة."
    )
    countdown_message = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=initial_text,parse_mode='Markdown',reply_markup=get_countdown_button(duration_seconds))
    # إرسال الرسالة مع زر للوقت المتبقي
    # countdown_message = bot.send_message(
    #     chat_id, initial_text, parse_mode='Markdown', 
    #     reply_markup=get_countdown_button(duration_seconds)
    # )

    # بدء خيط العد التنازلي
    if not massage_edita:
        massage_edita.append(countdown_message.message_id)
    threading.Thread(target=countdown, args=(chat_id, massage_edita[0], duration_seconds)).start()
    return duration_seconds
# دالة لإرجاع زر يحتوي على الوقت المتبقي
def get_countdown_button(duration_seconds):
    minutes, seconds = divmod(duration_seconds, 60)
    countdown_text = f"🕒 الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية."
    
    # إنشاء الزر
    markup = telebot.types.InlineKeyboardMarkup()
    countdown_button = telebot.types.InlineKeyboardButton(text=countdown_text, callback_data="remaining_time")
    markup.add(countdown_button)
    
    return markup

# دالة العد التنازلي وتحديث الرسالة
def countdown(chat_id, message_id, duration_seconds):
    global end_time  # استخدام end_time كمتغير عام
    # حساب end_time عند بدء العد التنازلي
    end_time = datetime.now(pytz.utc).astimezone(libya_timezone) + timedelta(seconds=duration_seconds)

    for remaining in range(duration_seconds, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        countdown_text = f"🕒 الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية."

        # حساب وقت الانتهاء بتوقيت ليبيا بتنسيق 12 ساعة
        remaining_time_str = end_time.strftime('%I:%M:%S')
        am_pm = get_arabic_am_pm(end_time.hour)

        # نص الرسالة المحدث مع وقت انتهاء المسابقة
        updated_text = (
            f"🎉 المسابقة بدأت الآن! 🎉\n"
            f"⏰ ستنتهي المسابقة في {remaining_time_str} {am_pm} بتوقيت ليبيا.\n"
            f"{countdown_text}"
        )
        tim = f"{remaining_time_str} {am_pm}"
        
        try:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=updated_text,
                reply_markup=get_countdown_button(remaining),
                parse_mode='Markdown'
            )
        except telebot.apihelper.ApiException:
            # استدعاء الدالة لإنشاء الرسالة من جديد في حالة الحذف
            message_id = restart_countdown_message(chat_id, remaining)

        time.sleep(1)

    # إرسال رسالة تنبيه بانتهاء المسابقة
    if candidates:
        for user_id in user_votes.keys():
            delete_old_messages(user_id)
            if user_id not in admin:
                bot.send_message(user_id, "لقد انتهت المسابقة، وسيتم الإعلان عن الفائز قريبًا.🕑")

        # إنشاء الأزرار للقائمة النهائية بعد انتهاء المسابقة
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = KeyboardButton(boten_key_name.get("add_user"))
        button2 = KeyboardButton(boten_key_name.get("add_admin"))
        button3 = KeyboardButton(boten_key_name.get("view_vote"))
        button4 = KeyboardButton(boten_key_name.get("settings"))
        button5 = KeyboardButton(boten_key_name.get("delet_user"))
        button6 = KeyboardButton(boten_key_name.get("delet_admin"))
        button7 = KeyboardButton(boten_key_name.get("add_button_key"))
        markup.add(button1, button2)
        markup.add(button3, button4)
        markup.add(button5, button6)
        markup.add(button7)

        # إرسال رسالة للمشرفين عند انتهاء المسابقة
        for chat_admin in admin:
            if chat_id == chat_admin:
                bot.send_message(chat_admin, f"تم إيقاف المسابقة وفقًا لطلبك الساعة {tim}🕗", reply_markup=markup)

        # تحديث المتغيرات بعد انتهاء المسابقة
        candidates1.clear()
        user_votes2.clear()
        candidates1.update(candidates)
        user_votes2.update(user_votes)
        user_votes.clear()
        candidates.clear()

        # حذف الرسالة النهائية للعد التنازلي
        bot.delete_message(chat_id, massage_edita[0])
def restart_countdown_message(chat_id, remaining_seconds):
    """
    دالة لإعادة إنشاء رسالة العد التنازلي في حالة حذفها من قبل المستخدم.
    """
    minutes, seconds = divmod(remaining_seconds, 60)
    countdown_text = f"🕒 الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية."

    # حساب وقت الانتهاء بتوقيت ليبيا بتنسيق 12 ساعة
    remaining_time_str = end_time.strftime('%I:%M:%S')
    am_pm = get_arabic_am_pm(end_time.hour)

    # نص الرسالة المحدث مع وقت انتهاء المسابقة
    updated_text = (
        f"🎉 المسابقة بدأت الآن! 🎉\n"
        f"⏰ ستنتهي المسابقة في {remaining_time_str} {am_pm} بتوقيت ليبيا.\n"
        f"{countdown_text}"
    )

    # إرسال رسالة جديدة عند حذف الرسالة الأصلية
    new_message = bot.send_message(
        chat_id=chat_id,
        text=updated_text,
        reply_markup=get_countdown_button(remaining_seconds),
        parse_mode='Markdown'
    )

    # تحديث قائمة الرسائل المتاحة ليتم تعديلها في الدورة القادمة
    massage_edita.clear()
    massage_edita.append(new_message.message_id)

    return new_message.message_id

def show_remaining_time(chat_id,call):
    if massage_edita:
        remaining_time = datetime.now(pytz.utc).astimezone(libya_timezone)
        if end_time:  # التحقق من أن end_time معرّف
            time_left = (end_time - remaining_time).total_seconds()
            if time_left > 0:
                minutes, seconds = divmod(int(time_left), 60)
                countdown_text = f"🕒 الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية."
                updated_text = (
                    f"🎉 المسابقة لا تزال مستمرة! 🎉\n"
                    f"{countdown_text}"
                )
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*{updated_text}*",parse_mode='Markdown')
            else:
                if candidates:
                    for user_id in user_votes.keys():
                        delete_old_messages(user_id)
                        if user_id not in admin:
                            bot.send_message(user_id, "لقد انتهت المسابقة، وسيتم الإعلان عن الفائز قريبًا.🕑")

                    # إنشاء الأزرار للقائمة النهائية بعد انتهاء المسابقة
                    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    button1 = KeyboardButton(boten_key_name.get("add_user"))
                    button2 = KeyboardButton(boten_key_name.get("add_admin"))
                    button3 = KeyboardButton(boten_key_name.get("view_vote"))
                    button4 = KeyboardButton(boten_key_name.get("settings"))
                    button5 = KeyboardButton(boten_key_name.get("delet_user"))
                    button6 = KeyboardButton(boten_key_name.get("delet_admin"))
                    button7 = KeyboardButton(boten_key_name.get("add_button_key"))
                    markup.add(button1, button2)
                    markup.add(button3, button4)
                    markup.add(button5, button6)
                    markup.add(button7)

                    # تحديث المتغيرات بعد انتهاء المسابقة
                    candidates1.clear()
                    user_votes2.clear()
                    candidates1.update(candidates)
                    user_votes2.update(user_votes)
                    user_votes.clear()
                    candidates.clear()
                    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="*⏰ انتهى وقت المسابقة.*",parse_mode='Markdown', reply_markup=markup)    
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="*⏰ انتهى وقت المسابقة.*",parse_mode='Markdown')
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="*لم يتم ضبط وقت انتهاء المسابقة بعد.*",parse_mode='Markdown')
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="*لم تبدأ أي مسابقة حاليًا.*",parse_mode='Markdown')
# دالة لتحويل الوقت المدخل (ساعة:دقيقة) إلى ثواني

def parse_duration(duration_str):
    try:
        # تقسيم المدخل لصيغة "ساعة:دقيقة"
        hours, minutes = map(int, duration_str.split(":"))
        total_seconds = (hours * 60 * 60) + (minutes * 60)
        return total_seconds
    except ValueError:
        # إذا كان الإدخال غير صحيح
        return None
def add_tiemr(message):
    tst = ["0:30","1:00","1:30","2:00"]
    text = message.text
    chat_id = message.chat.id
    if text:
        if validate_time_format(text):
            if  not ":" in text:
                bot.send_message(chat_id,"الرجاء ارسال الوقت بطريقه صحيحه مثلا\n12:00")
                return
            if text in tst or text in timers:
                bot.send_message(chat_id,"عذرا، تم اضافة هذا الوقت بلفعل ✅")
                return
            else:
                timers.append(text)
                bot.send_message(chat_id,"تم اضافة الوقف بنجاح ✅")
                keyboard = InlineKeyboardMarkup()

                # تصحيح الحقول إلى callback_data
                bt1 = InlineKeyboardButton("نص ساعة، 0:30", callback_data=f"tims_0:30")
                bt2 = InlineKeyboardButton("ساعة، 1:00", callback_data=f"tims_1:00")
                bt3 = InlineKeyboardButton("ساعة ونص، 1:30", callback_data=f"tims_1:30")
                bt4 = InlineKeyboardButton("ساعتان، 2:00", callback_data=f"tims_2:00")

                # إضافة الأزرار إلى لوحة المفاتيح المضمنة
                keyboard.add(bt1)
                keyboard.add(bt2, bt3)
                keyboard.add(bt4)
                keyboard.add(InlineKeyboardButton("اضافة وقت اخر", callback_data=f"tim_adde"))
                if timers:
                    for x in timers:
                        keyboard.add(InlineKeyboardButton(f"{x}", callback_data=f"tims_{x}"))
                # تعديل الرسالة وإضافة لوحة المفاتيح المضمنة
                bot.send_message(chat_id=chat_id, text=f"*متى تريد ان تنتهي المسابقة؟*", parse_mode='Markdown', reply_markup=keyboard)


        else:
            bot.send_message(chat_id,"خطاء ❌،الرجاء التأكد من النص وارسله المره القادمه")        
def validate_time_format(time_str):
    # التعبير المنتظم للتحقق من أن النص هو بصيغة "HH:MM"
    pattern = r'^([0-9]|[01]\d|2[0-3]):([0-5]\d)$'
    
    # التحقق من المطابقة
    match = re.match(pattern, time_str)
    
    if match:
        return True  # إذا كان النص مطابقًا للصيغة المطلوبة
    else:
        return False  # إذا كان النص غير مطابق
