from info import *
# مرجع قاعدة البيانات
db_ref = db.reference("groups")
# تشغيل Telethon
#telethon_client.start()
warnings = {}
start_text = []
admin = [admin_aq]
GRoup = []
keyls = []
Valuels = []
markup_key = []
key_keu = []
photo_url = []
user_chat_admin = []
channels = []
rednmper = []
sand_all = []
reply_ms = []
Button =[]
boten_neame =[]
message_ass =[]
message_ass1 =[]
boten_neame_text = {}
text_boten =[]
مسار_الصورة =[]
fldars =[]
chat_ida =[]
user_votes2 =[]
Group_idE = []
fja = []
send_photo = []
user_Mute = set()
user_Mute_tame = {}
attempt_count = 0
cout = 1
Enter_add_info = []
fousol = {
    1: "الفصل الأول",
    2: "الفصل الثاني",
    3: "الفصل الثالث",
    4: "الفصل الرابع",
    5: "الفصل الخامس",
    6: "الفصل السادس",
    7: "الفصل السابع",
    8: "الفصل الثامن",
    9: "الفصل التاسع",
    10: "الفصل العاشر"
}

college_departments = {
    "القسم العام",
    "علوم الحاسب",
    "تقنية المعلومات" ,
    "الذكاء الاصطناعي",
    "شبكات الحاسب",
    "نظم المعلومات"
}
General_sec = {
    "الفصل الأول": {
        "ARAB155": "لغة عربية",
        "ENG151": "اللغة الإنجليزية 1",
        "Cl103": "رياضيات عامة 1",
        "Cl104": "إحصاء واحتمالات",
        "Cl101":"مقدمة لعلم الحاسوب",
        "Cl102": "برمجة 1",
    },
    "الفصل الثاني": {
        "Cl111": "تطبيقات الحاسوب",
        "ENG152": "اللغة الإنجليزية 2",
        "Cl113": "رياضيات عامة 2",
        "Cl114": "طرق احصائية",
        "CI112": "برمجة 2",
        "CI115":"فيزياء عامة",
        "CI116": "معمل فيزياء",
    },
    "الفصل الثالث": {
        "CN201": "مقدمة لشبكات الحاسوب",
        "IT201": "هياكل بيانات وتطبيقات",
        "CS202": "تصميم الدارات الرقمية",
        "CI202": "طرق عددية",
        "IS201": "نظم المعلومات",
        "CI203": "تقنيات كتابية",
    }
}

college_departments = {
    "القسم العام" : General_sec,
}


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
def tset_next_massage(message):
    text = message.text
    if text in ["اضافة ادمن","حذف ادمن","الإحصائية 📊",'اعدادات البوت']:
        return True
def masage_text_next(message):
    text = message.text
    chat_id = message.chat.id
    try:
        if text in ["اضافة ادمن","حذف ادمن","الإحصائية 📊",'اعدادات البوت']:
            handle_all_messages1(message)
    except Exception as e :
        print(e)
def examine(user_id):
    ref = db.reference(f'/users/{user_id}')
    data = ref.get()
    for key,Value in data.items():
        keyls.append(key)
        Valuels.append(str(Value))
    db.reference(f'/Aministrtor/{int(user_id)}').set({
                    keyls[1]: Valuels[1],
                    keyls[5]: Valuels[5],
                    keyls[4]: Valuels[4],
                    keyls[3]: Valuels[3],
                    keyls[0]: Valuels[0],
                    })
    keyls.clear() ; Valuels.clear() 
class Admin:
    def __init__(self, bot, admin_list):
        self.bot = bot
        self.admin_list = admin_list
        self.admin_list.clear()
        admin.append(developer)
        ref = db.reference(f'/Aministrtor')
        data = ref.get()
        if data is None:
            examine(developer)
            return
        try:
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
    ref = db.reference(f'/users/{chat_id}')
    data = ref.get()
    if data:
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
    text = f"""{text}"""
    chat_id = user.id
    text_x = edit_text_start(message,text,chat_id)
    start_text.append(text)
    db.reference(f'/Welcome Message/').set({
                 "Message" : text,
                'created_at': created_at
                })
    bot.send_message(chat_id,f"تم اضافة رسالة الترحيب بنجاح ✅\n شكل رسالة الترحيب التي تظهر للمستخدم\n {text_x}",parse_mode='Markdown') 
boten_key_name = {
    "add_admin" : 'اضافة ادمن',
    "delet_admin": 'حذف ادمن',
    "view_vote" : 'الإحصائية 📊',
    "settings"  : 'اعدادات البوت',
}        

def handle_all_messages1(message):
    global Enter_add_info
    chat_id = message.from_user.id
    text = message.text
    is_admin = admin_chat.admin_start(chat_id)
    ref = db.reference(f'/SuperTS/{chat_id}')
    data = ref.get()
    if data is not None or is_admin:
            if text == "اضافة البيانات":
                bot.send_message(chat_id,"*الآن، سأتابع معك خطوة بخطوة. أولاً، سنضيف المجموعة،يرجى إضافة البوت إلى المجموعة وترقيته إلى مشرف.*",parse_mode='Markdown')
                Enter_add_info.append(True)
                print(Enter_add_info)
    if is_admin:
        if text == boten_key_name.get("add_admin"):
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='عرض قائمة الادمن', callback_data='arad_admin')
            btn2 = InlineKeyboardButton(text='اضافة ادمن', callback_data='add_next_admin')
            keyboard.add(btn1)
            keyboard.add(btn2)
            keyboard.add(InlineKeyboardButton("اضافة مشرف",callback_data ="add_mshrf"))
            bot.send_message(chat_id,"اختر احد من الخيارات الاتيه",reply_markup=keyboard)
        elif text == boten_key_name.get("view_vote"):
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text="عرض المجموعات", callback_data='viewa_tsoey')
            btn2 = InlineKeyboardButton(text=" الكاملة", callback_data='stetes')
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
        elif text == boten_key_name.get("delet_admin"):
            if chat_id != admin[0] and chat_id:
                
                bot.send_message(chat_id,"عذرآ، لا يمكنك حذف اي ادمن لان ليس لديك الصلاحيات الكافيه وحده المطور الاساسي هو من لديه هذه الصلاحية.")
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
def add_moshraf(message):
    text = message.text
    user_id = message.chat.id
    tset = tset_next_massage(message)
    if tset == True:
        masage_text_next(message)
        return
    ref = db.reference(f'/users/')
    data = ref.get()
    if data is None:
        bot.send_message(user_id,"عذرا، لايوجد مستخدمين في قاعدة البيانات.")
        return
    if text:
            if not text.startswith("@") and not text.isdigit():
                bot.send_message(user_id,"عذرا، الرجاء اضافة علامة @ قبل اليوزر✅")
                return
            if text.startswith("@"):
                for user_id in data:
                    ref = db.reference(f'/users/{user_id}')
                    data = ref.get()
                    for key , valuo in dict(data).items():
                        if f"@{valuo}" == text:
                            db.reference(f'/SuperTS/{user_id}').set({
                            'created_at': created_at
                            })
                            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                            button1 = KeyboardButton("اضافة البيانات")
                            user = bot.get_chat(user_id)
                            first_name = user.first_name if user.first_name else "بدون اسم اول"
                            last_name = user.last_name if user.last_name else "بدون اسم ثاني"
                            full_name = f"{first_name} {last_name}" if last_name else first_name
                            username = user.username if user.username else "بدون يوزر"
                            markup.add(button1)
                            bot.send_message(admin[0],"تمت ترقية المستخدم الي مشرف وتم اخباره بذلك✅")
                            bot.send_message(user_id,f"مرحبًا بك يا {full_name}!\nتمت ترقيتك إلى مشرف في البوت. الآن يمكنك إدارة مجموعتك باستخدام البوت.",reply_markup=markup,parse_mode='Markdown')
                            return
            elif isinstance(text, int):
                for user_id in data:
                        if int(user_id) == text:
                            db.reference(f'/Supervisor/{user_id}').set({
                            'created_at': created_at
                            })
                            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                            button1 = KeyboardButton("اضافة البيانات")
                            markup.add(button1)
                            user = bot.get_chat(user_id)
                            first_name = user.first_name if user.first_name else "بدون اسم اول"
                            last_name = user.last_name if user.last_name else "بدون اسم ثاني"
                            full_name = f"{first_name} {last_name}" if last_name else first_name
                            username = user.username if user.username else "بدون يوزر"
                            bot.send_message(user_id,f"*مرحبًا بك يا {full_name}!\nتمت ترقيتك إلى مشرف في البوت. الآن يمكنك إدارة مجموعتك باستخدام البوت.*",reply_markup=markup,parse_mode='Markdown')
def generate_random_code():
    # الأحرف الممكنة مع الأرقام
    characters = string.ascii_uppercase + string.digits
    # إنشاء أقسام الكود
    part1 = 'ALWS'  # ثابت
    part2 = ''.join(random.choices(characters, k=3))
    part3 = ''.join(random.choices(characters, k=4))
    part4 = ''.join(random.choices(characters, k=4))
    part5 = ''.join(random.choices(characters, k=3))
    # تجميع الكود
    return f"{part1}-{part2}-{part3}-{part4}-{part5}"
# دالة فك الكتم عن المستخدم
def unmute_user(chat_id, duration):
    global attempt_count
    time.sleep(duration)
    attempt_count = 0
    user_Mute.remove(chat_id)
# معالجة الصورة المستلمة
def process_photo(message, chat_id):
    global attempt_count, send_photo

    # التحقق من حالة المستخدم (هل مكتوم)
    if chat_id in user_Mute:
        elapsed_time = time.time() - user_Mute_tame[chat_id]
        remaining_time = max(0, 3600 - elapsed_time)
        minutes, seconds = divmod(int(remaining_time), 60)
        bot.send_message(chat_id, f"لقد استنفدت جميع محاولاتك، انتظر لمدة {minutes}:{seconds} 🕘✅")
        return

    # التحقق من عدد المحاولات
    if send_photo and chat_id in send_photo:
        attempt_count += 1
        if attempt_count >= 5:
            threading.Thread(target=unmute_user, args=(chat_id, 3600)).start()
            bot.send_message(chat_id, "لقد استنفدت جميع محاولاتك، انتظر لمدة ساعة 🕘✅")
            user_Mute.add(chat_id)
            user_Mute_tame[chat_id] = time.time()
            return

    # تحميل الصورة ومعالجتها
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"{uuid.uuid4()}.png"
    save_path = os.path.join(os.getcwd(), file_name)
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    try:
        # قراءة النصوص باستخدام OCR
        image = Image.open(save_path)
        extracted_text = pytesseract.image_to_string(image, lang='ara')
        ocr = PaddleOCR(use_angle_cls=False, lang='en', show_log=False)
        ocr_result = ocr.ocr(save_path, cls=True)

        # استخراج البيانات
        courses, student_name, student_id = extract_data(extracted_text, ocr_result)
        if not student_name or not student_id:
            send_photo.append(chat_id)
            bot.reply_to(message, "عذرًا، الصورة غير واضحة أو لا تحتوي على معلومات.")
            os.remove(save_path)
            return

        # التحقق من حالة المستخدم والمادة
        if not validate_user_courses(chat_id, courses):
            send_photo.append(chat_id)
            bot.reply_to(message, f"عذرًا، لا توجد لديك المادة المقررة أو أنها غير واضحة.")
            os.remove(save_path)
            return

        # فك الكتم عن المستخدم
        unrestrict_user(chat_id, save_path, student_name, student_id)

    finally:
        # حذف الملف بعد الاستخدام
        if os.path.exists(save_path):
            os.remove(save_path)

# استخراج البيانات من النصوص
def extract_data(extracted_text, ocr_result):
    courses = []
    student_name, student_id = None, None

    # استخراج النصوص ذات الصلة
    
    for line in ocr_result[0]:
        text = line[1][0]
        if text.startswith(("CI", "ENG", "ARAB", "CN", "IT", "CS", "IS", "AI", "NT")) and len(text) in [5, 6, 7]:
            print(text)
            courses.append(text)

    # تحليل النصوص لاستخراج اسم ورقم الطالب
    for line in extracted_text.split("\n"):
        if "اسم الطالب" in line:
            student_name = line.split(":")[-1].strip()
        elif "رقم الطالب" in line:
            student_id = line.split(":")[-1].strip()

    return courses, student_name, student_id

# التحقق من وجود المادة المقررة
def validate_user_courses(chat_id, courses):
    ref = db.reference('/Supervisor')
    data = ref.get()
    if data is None:
        bot.send_message(admin[0], "لا توجد قاعدة بيانات لقراءتها.")
        return False

    for group_id, group_data in data.items():
        if chat_id in group_data.get("members", []):
            subject = group_data.get("subject", "")
            if subject in courses:
                return True
    return False

# فك الكتم عن المستخدم
def unrestrict_user(chat_id, file_path, student_name, student_id):
    try:
        permissions = ChatPermissions(can_send_messages=True)
        bot.restrict_chat_member(chat_id, chat_id, permissions=permissions)
        bot.send_message(chat_id, f"تم فك كتمك بنجاح ✅\nاسم الطالب: {student_name}\nرقم الطالب: {student_id}")
    except Exception as e:
        print(f"خطأ أثناء فك الكتم: {e}")
        return
def add_new_user(chat_id, full_name, username, language, is_bot):
    joining_data = rest(chat_id)
    db.reference(f'/users/{chat_id}').set({
        'full_name': full_name,
        'username': username,
        'language': language,
        "joining": joining_data,
        "is_Bot": is_bot,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def send_welcome_message(chat_id, message):
    ref = db.reference('/Welcome Message/')
    data = ref.get()

    if start_text:
        text = edit_text_start(message, start_text[0], chat_id)
    elif data and "Message" in data:
        text = edit_text_start(message, data["Message"], chat_id)
        start_text.append(text)
    else:
        text = "مرحبًا بك في البوت!"

    bot.send_message(chat_id, text, parse_mode='Markdown')


def handle_existing_user(chat_id, message, is_admin, full_name):
    if message.text.startswith('/start'):
        if is_admin:
            send_admin_panel(chat_id, full_name)
        else:
            send_welcome_message(chat_id, message)

    elif message.text.startswith('/id'):
        bot.reply_to(message, f"*YOUR ID* : `{chat_id}`", parse_mode='Markdown')

    elif message.text.startswith('/help'):
        bot.reply_to(message, "إذا كان هناك خطأ، الرجاء التواصل مع المطور: @ko_2s")
def send_admin_panel(chat_id, full_name):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(
        KeyboardButton("اضافة ادمن"),
        KeyboardButton("حذف ادمن"),
        KeyboardButton("الإحصائية 📊"),
        KeyboardButton('اعدادات البوت')
    )
    bot.send_message(chat_id, f"مرحبا بك يا أدمن 🤍\n{full_name}\nاختر أحد الخيارات ليتم تنفيذها:", reply_markup=markup)    
def manage_members(message: Message):
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
