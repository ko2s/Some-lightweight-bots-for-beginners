import telebot
from telebot import types
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timezone
import random
import string

load_dotenv()
urlbass = os.getenv('url_firbass')
# تحديد الوقت الحالي بالتوقيت العالمي (UTC)
created_at = datetime.now(timezone.utc).isoformat()
# تهيئة Firebase
cred = credentials.Certificate("libya-f6bc1-firebase-adminsdk-wdmyu-50388bb16c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': urlbass  # استبدل بالـ URL الخاص بمشروعك
})


BOT_TOKEN = os.getenv('bot_test')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in .env file")

bot_ms = telebot.TeleBot(BOT_TOKEN)

admin_chat_id = os.getenv('admin_id')
if admin_chat_id:
    admin_chat_id = int(admin_chat_id)
channels = ["@Qran_krem_1", "@br1mg"]
def is_admin(user_id):
    global admin_ids
    admin_ids = admin_chat_id # ضع معرفات المديرين هنا
    return user_id in admin_ids
def check_user_registration(user_id):
    ref = db.reference(f'/users/{user_id}')
    return ref.get() is not None

is_bot_running = True
edite = True

class UserState:
    def __init__(self):
        self.level = None  # تأكد من وجود الخاصية level
        self.subject = None
        self.score_ratio = None



preparatory_scores = {
    "التربية الإسلامية": 56,
    "النحو": 112,
    "الكتابة": 56,
    "اللغة الإنجليزية": 112,
    "الحاسوب": 56,
    "الرياضيات": 140,
    "العلوم": 140,
    "التاريخ": 56,
    "الجغرافيا": 56
}

secondary_scores = {
    "التربية الإسلامية": 56,
    "اللغة العربية": 112,
    "اللغة الإنجليزية": 112,
    "تقنية معلومات": 56,
    "الرياضيات": 140,
    "الاحصاء": 56,
    "الفيزياء": 140,
    "الكيمياء": 112,
    "الاحياء": 112
}
secondary_scores_ad = {
    "التربية الإسلامية": 56,
    "اللغة العربية": 196,
    "اللغة الإنجليزية": 140,
    "تقنية معلومات": 56,
    "الاحصاء": 56,
    "التاريخ": 84,
    "الجغرافيا": 84,
    "الفلسفة": 84,
    "علم الاجتماع": 56,
    "علم النفس": 56,


}
thanoe_exam_ad = {
    1 : "التربية الإسلامية",
    2 : "اللغة العربية",
    3 : "اللغة الإنجليزية",
    4 : "تقنية معلومات",
    5 : "الاحصاء",
    6 : "التاريخ",
    7 : "الجغرافيا",
    8 : "الفلسفة",
    9 : "علم الاجتماع",
    10 : "علم النفس"
}

thanoe_exam = {
    1: "التربية الإسلامية",
    2: "اللغة العربية",
    3: "اللغة الإنجليزية",
    4: "تقنية معلومات",
    5: "الرياضيات",
    6: "الاحصاء",
    7: "الفيزياء",
    8: "الكيمياء",
    9: "الاحياء"
}

adade_exam = {
    1: "التربية الاسلامية",
    2: "النحو والقراءة والنصوص",
    3: "الكتابة",
    4: "اللغة الانجليزية",
    5: "الحاسوب",
    6: "الرياضيات",
    7: "العلوم",
    8: "التاريخ",
    9: "الجغرافيا"
}

thanoe_ad = {
    1: "*ادخال درجات الامتحان التربية الاسلامية*",
    2: "*ادخال درجات الامتحان اللغة العربية*",
    3: "*ادخال درجات الامتحان اللغة الانجليزية*",
    4: "*ادخال درجات الامتحان تقنية معلومات*",
    5: "*ادخال درجات الامتحان الاحصاء*",
    6: "*ادخال درجات الامتحان التاريخ*",
    7: "*ادخال درجات الامتحان الجغرافيا*",
    8: "*ادخال درجات الامتحان الفلسفة*",
    9: "*ادخال درجات الامتحان علم الاجتماع*",
    10: "*ادخال درجات الامتحان علم النفس*"
}

thanoe_work_ad = {key: value.replace("الامتحان", "اعمال") for key, value in thanoe_ad.items()}
thanoe = {
    1: "*ادخال درجات الامتحان التربية الاسلامية*",
    2: "*ادخال درجات الامتحان اللغة العربية*",
    3: "*ادخال درجات الامتحان اللغة الانجليزية*",
    4: "*ادخال درجات الامتحان تقنية معلومات*",
    5: "*ادخال درجات الامتحان الرياضيات*",
    6: "*ادخال درجات الامتحان الاحصاء*",
    7: "*ادخال درجات الامتحان الفيزياء*",
    8: "*ادخال درجات الامتحان الكيمياء*",
    9: "*ادخال درجات الامتحان الاحياء*",
}

thanoe_work = {key: value.replace("الامتحان", "اعمال") for key, value in thanoe.items()}

adade = {
    1: "*ادخال درجات الامتحان التربية الاسلامية*",
    2: "*ادخال درجات الامتحان النحو والقراءة والنصوص*",
    3: "*ادخال درجات الامتحان الكتابة*",
    4: "*ادخال درجات الامتحان اللغة الانجليزية*",
    5: "*ادخال درجات الامتحان الحاسوب*",
    6: "*ادخال درجات الامتحان الرياضيات*",
    7: "*ادخال درجات الامتحان العلوم*",
    8: "*ادخال درجات الامتحان التاريخ*",
    9: "*ادخال درجات الامتحان الجغرافيا*"
}

adade_work = {key: value.replace("الامتحان", "اعمال") for key, value in adade.items()}

thanoe_min_scores = {
  1: 40, 2: 80, 3: 80, 4: 40, 5: 100,
  6: 40, 7: 100, 8: 80, 9: 80
}
thanoe_min_scores_ad = {
  1: 40, 2: 140, 3: 100, 4: 40, 5: 40,
  6: 60, 7: 60, 8: 60, 9: 40, 10 : 40
}
adade_min_scores = {
    1: 40, 2: 80, 3: 40, 4: 80, 5: 40,
    6: 100, 7: 100, 8: 40, 9: 40
}

user_scores = {}
user_work_scores = {}
current_step = {}
exam_type = {}
student_ids = {}
last_question = {}
last_message = {}
is_exam = {}
user_states = {}
delet = []
delet2 = []
edit=[]
gred = []
delettt = []
reply_ms = []
def create_subjects_markup(subjects):
    markup = ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    for subject in subjects:
        markup.add(KeyboardButton(subject))
    return markup

@bot_ms.message_handler(commands=["start", "math", "id", "admin", "command","stop","help","aqila","get_id","edit_id","send"])
def welcm(message):
    global delettt
    user_id = message.from_user.id
    # تخزين المستخدم في `users_all`
    db.reference(f'/users_all/{user_id}').set({
            'used_by': user_id,
            'created_at': created_at
        })
    chat_id = message.from_user.id
    if not check_subscription(chat_id):
        send_subscription_message(chat_id)
        return


    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = f"{first_name} {last_name}" if last_name else first_name
    bot_ms_info = bot_ms.get_me()
    bot_ms_name = bot_ms_info.first_name
    admin_chat = bot_ms.get_chat(admin_chat_id) #هذه الطريقة لي جلب معلومة معيننه من الادمن
    admin_name = admin_chat.last_name
    admin_user = admin_chat.username
    if message.text.startswith('/start'):
        bot_ms.send_message(chat_id, f"\nمرحبا بك يا {full_name}❤️\n"
                                      f"في بوت {bot_ms_name}🤍\n"
                                      "مطور ومبرمج البوت 👨‍💻🤍\n"
                                      f"[{admin_name}](https://t.me/aUSER_telebot)\n"
                                      "*يمكنك طلب اي بوت يمكن برمجته *[هنا](https://wa.me/218918490176)👨‍💻💬.",
                             parse_mode='Markdown')
    elif message.text.startswith("/help"):
        bot_ms.send_message(chat_id,f"""،مرحبا يا {full_name}🤍

* سأعرفك بـ كل أمر : *

*- أمر /start *  : هو أمر لبدء البوت.
*- أمر /admin *  : هو أمر لطلب المساعدة من الأدمن. في كثير من الأحيان تحدث أخطاء في بوتات تيليجرام، ويكون الخطأ عشوائيًا ناتجًا عن التصادم بالنظام أو سوء استخدام أو غيره. لذلك، عندما تكتب أمر /admin، يتم استدعاء الأدمن لحل المشكلة، طبعًا بعد الضغط على "نعم" لتأكيد الطلب.
*- أمر /math *  : هو الأمر الرئيسي الذي من أجله تم إنشاء هذا البوت. يقوم بحساب نتيجتك في أي من الشهادتين بعد إدخال جميع البيانات بشكل صحيح. عند كتابة أمر /math، تظهر لك رسالة تطلب منك إدخال رقم الجلوس لمرة واحدة. هناك الكثير يتساءل عن فائدة رقم الجلوس في هذا البوت، ونحن نعمل بشكل مستمر لجعل رقم الجلوس له قيمة مميزة في البوت. سيكون البوت من البوتات المميزة في دولتنا الحبيبة ليبيا 🇱🇾. لا أستطيع الإفصاح عن التفاصيل حاليًا، لكن سيكون له دور مميز بعد استكمال الإجراءات اللازمة.
*- أمر /id *  : هو أمر لجلب رقم حسابك على تيليجرام، أو كما يُعرف بـ ID حسابك.
*- أمر /grades  : * هو أمر مميز حيث يمكنك من حساب درجتك في الامتحان، وعدد الدرجات لكل سؤال والنسبة المئوية لك في المادة. هذه النسبة مهمة عند التقديم في معاهد مثل معهد النفط، حيث يجب أن تكون نسبتك في العلوم والرياضيات 65% كما يُقال .
*- أمر /stop *  : هو أمر لإيقاف أي عملية تحدث على البوت مثل عملية /math وعملية /grades.
*- أمر /command *  : هو أمر لإضافة تعليق حول البوت. هذا يساعد في نجاح هدف البوت ومواكبة التطور العلمي، حيث أن كل تعليق يمكن أن يؤثر في تحسين مستوى البوت.
*- أمر /edit_id * : هو امر لي جلب رقم جلوسك اذا نسيته                             """,parse_mode='Markdown')
    elif message.text.startswith("/math"):
        # الجزء الثاني من الكود
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='ثانوية', callback_data='thanoe_al')
        btn2 = telebot.types.InlineKeyboardButton(text='اعدادية', callback_data='adade')
        keyboard.add(btn1, btn2)
        msg = bot_ms.send_message(chat_id, "حدد مستواك التعليمي", reply_markup=keyboard)

        # إذا كان هناك رسالة /math سابقة، احذفها واحتفظ بالرسالة الأخيرة فقط
        if chat_id in last_message:
            try:
                bot_ms.delete_message(chat_id, last_message[chat_id])
            except Exception as e:
                pass

        # حفظ معرف الرسالة الأخيرة
        last_message.clear()
        last_message[chat_id] = msg.message_id

        # تنظيف قائمة edit والاحتفاظ بالرسالة الأخيرة فقط
        edit.clear()
        edit.append(msg.message_id)   # تجاهل الخطأ إذا كانت الرسالة قد حذفت مسبقًا


    elif message.text.startswith('/id'):
        user_id = message.from_user.id
        bot_ms.reply_to(message, f"*YOUR ID* : "f'`{user_id}`', parse_mode='Markdown')
    elif message.text.startswith('/stop'):
        time.sleep(0.5)
        bot_ms.reply_to(message,"تم ايقاف العملية بنجاح. ")
    elif message.text.startswith('/admin'):
        chat_id = message.chat.id
        user_id = message.from_user.id
        full_name = message.from_user.first_name

        # إنشاء لوحة مفاتيح لخيارات نعم ولا
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn_yes = telebot.types.InlineKeyboardButton(text='نعم', callback_data='notify_admin_yes')
        btn_no = telebot.types.InlineKeyboardButton(text='لا', callback_data='notify_admin_no')
        keyboard.add(btn_yes, btn_no)

        # حذف الرسالة السابقة الخاصة بأمر /admin إذا كانت موجودة
        if chat_id in last_message:
            try:
                bot_ms.delete_message(chat_id, last_message[chat_id])
            except Exception as e:
                pass

        # إرسال الرسالة الجديدة وحفظ معرفها
        msg = bot_ms.reply_to(message,
            f'مرحبا يا :\t {full_name} \n\tيوزرك : {"@" + (message.from_user.username or "بدون يوزر")}\t\nهل تريد اخبار الادمن ليصلح مشكلة ما في المحادثة؟',
            reply_markup=keyboard
        )

        # حفظ معرف الرسالة الجديدة
        last_message.clear()
        last_message[chat_id] = msg.message_id


    elif message.text.startswith('/send'):
        bot_ms.reply_to(message,"تم ايقاف امر /send \nسوف يتم استئناف الامر يوم النتيجة")

    elif message.text.startswith('/command'):
        chat_id = message.chat.id

        # إذا كان هناك رسالة سابقة مرتبطة بالأمر /command، حذفها
        if chat_id in last_message:
            try:
                bot_ms.delete_message(chat_id, last_message[chat_id])
            except Exception as e:
                pass

        # إرسال الرسالة الجديدة وحفظ معرف الرسالة
        msg = bot_ms.send_message(chat_id, "اضف تعليق يمكن أن يحسن البوت 🤍✨ ")

        # حفظ معرف الرسالة الجديدة في القاموس
        last_message[chat_id] = msg.message_id

        # تسجيل المتابعة للتعليق الجديد
        bot_ms.register_next_step_handler(msg, handle_command)
    elif message.text.startswith('/aqila'):
           if (message.from_user.id) == admin_chat_id:
               # إنشاء لوحة المفاتيح
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                # إنشاء الأزرار
                button1 = KeyboardButton('create_code')
                button2 = KeyboardButton('search')
                button3 = KeyboardButton('code_all')
                button4 = KeyboardButton('user_all')
                button5 = KeyboardButton('reply')


                # إضافة الأزرار إلى لوحة المفاتيح
                markup.add(button1, button2)
                markup.add(button3, button4)
                markup.add(button5)

                # إرسال الرسالة مع لوحة المفاتيح
                bot_ms.send_message(message.chat.id, "اختر أحد الخيارات:", reply_markup=markup)

    elif message.text.startswith('/get_id'):
        user_id = message.from_user.id
        get_user_seat_number(user_id)
        bot_ms.reply_to(message, f"رقم جلوسك: `{seat_number}`",parse_mode='Markdown')
    elif message.text.startswith('/edit_id'):
        chat_id = message.chat.id
        user_id = message.from_user.id
        full_name = message.from_user.first_name

        # حذف الرسالة السابقة الخاصة بأمر /edit_id إذا كانت موجودة
        if chat_id in last_message:
            try:
                bot_ms.delete_message(chat_id, last_message[chat_id])
            except Exception as e:
                pass

        # إرسال الرسالة الجديدة وحفظ معرفها
        delett = bot_ms.send_message(chat_id,f"*مرحبا يا {full_name}\n الرجاء ارسال الكود الذي استلمته من الادمن \n اذا لم تستلم الكود الرجاء التوصل مع الادمن عن طريق \n امر /admin او عن طريق التوصل معه مباشرة @{admin_user}\n ملاحظة : الكود مجاني لكن ينطلب مره واحده فقط 🤍*",parse_mode='Markdown')

        # تخزين معرف الرسالة الجديدة
        last_message.clear()
        last_message[chat_id] = delett.message_id
        delettt.append(delett.message_id)
        if message.text == '/admin':
                return
        elif message.text == '/stop':
            botdel = bot_ms.reply_to(message,"تم الايقاف :")
            botdel = botdel.message_id
            time.sleep(2)
            bot_ms.delete_message(user_id,botdel)
            return
        else:
            bot_ms.register_next_step_handler(message, enter_seat_number)
            try:
                if len(delettt) >0:
                    delettt.clear()
                    delettt.append(delett.message_id)
            except Exception as e:
                    pass
@bot_ms.message_handler( content_types=['photo'])
def photo_message(message):
    chat_id = message.from_user.id
    bot_ms.send_message(chat_id, "*عذرًا، لا يمكنك إرسال الصور. \n هذه الميزة غير متوفرة في البوت. \n إذا أردت معرفة كيفية حساب نسبتك،\n اكتب `نسبتي` 🤍*",parse_mode='Markdown')
@bot_ms.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text
    chat_id = message.from_user.id
    if not check_subscription(chat_id):
        send_subscription_message(chat_id)
        return
    if not is_bot_running:
        return
    user_state = user_states.get(message.chat.id, UserState())

    if message.text == "/grades":
        send_levels(message)
    elif 'شرط النجاح'== message.text:
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='ثانوية', callback_data='thanoe1')
        btn2 = telebot.types.InlineKeyboardButton(text='اعدادية', callback_data='adade1')
        keyboard.add(btn1, btn2)
        msg = bot_ms.send_message(chat_id, "حدد مستواك التعليمي", reply_markup=keyboard)
    elif message.text ==('code_all'):
          scode1 = ''
          if (message.from_user.id) == admin_chat_id:
            try:
                ref = db.reference(f'/codes/')
                data = ref.get()
                n =0
                for scode in data :
                    if n == 0:
                        scode1 = scode    
                    else:    
                      scode1 = (f'`{scode}`') + "\n" + (f'`{scode1}`')+"\n"
                    n+=1
                scode1 = f'*عداد الاكود التي تم انشاءها : {n+1} *\n'+scode1
                bot_ms.send_message(admin_chat_id,scode1,parse_mode='Markdown')
            except Exception as e:
                bot_ms.send_message(admin_chat_id, "لا يوجد اكواد :")
    elif message.text==('create_code'):
        if chat_id == admin_chat_id:
            markup = types.InlineKeyboardMarkup()
            create_code_button = types.InlineKeyboardButton("إنشاء كود جديد", callback_data="create_new_code")
            markup.add(create_code_button)
            bot_ms.send_message(admin_chat_id, "اضغط على الزر لإنشاء كود جديد:", reply_markup=markup)
        else:
            bot_ms.send_message(admin_chat_id, "هذا الأمر مخصص للمدير فقط.")
    elif message.text==('search'):
        if chat_id == admin_chat_id:
            msg = bot_ms.send_message(admin_chat_id, "أرسل لي ID المستخدم للبحث:")
            bot_ms.register_next_step_handler(msg, search_user_by_id)
        else:
            bot_ms.send_message(message.chat.id, "هذا الأمر مخصص للمدير فقط.")
    elif message.text==('user_all'):
         if chat_id == admin_chat_id:
          mss = bot_ms.send_message(admin_chat_id,"*الرجاء ارسال الرسالة ليتم ارسلها لي جميع المستخدمين : *",parse_mode='Markdown')
          bot_ms.register_next_step_handler(mss, sned_all_user)
    elif message.text == 'شهادة اعدادية':
        user_state.level = 'شهادة اعدادية'
        user_states[message.chat.id] = user_state
        subjects = list(preparatory_scores.keys())
        markup = create_subjects_markup(subjects)
        bot_ms.send_message(message.chat.id, "اختر المادة:", reply_markup=markup)

    elif message.text == 'شهادة ثانوية':
        user_state.level = 'شهادة ثانوية'
        user_states[message.chat.id] = user_state
        keyboard = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        btn1 = KeyboardButton('ثانوية علمي')
        btn2 = KeyboardButton('ثانوية أدبي')
        keyboard.add(btn1, btn2)
        bot_ms.send_message(message.chat.id, "حدد نوع الشهادة الثانوية:", reply_markup=keyboard)
    elif message.text == ('reply'):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("حذف 🗑", callback_data="rep_dl")
        button2 = types.InlineKeyboardButton("تعديل 📝", callback_data="rep_ed")
        button3 = types.InlineKeyboardButton("اضافة 📥", callback_data="rep_end")
        button4 = types.InlineKeyboardButton("اضافة بوتن 📥", callback_data="rep_butm")
        markup.add(button2,button1)
        markup.add(button3)
        markup.add(button4)

        bot_ms.send_message(message.chat.id, "اختر اي من الاخيرات الاتيه ✅", reply_markup=markup)
    elif message.text == 'ثانوية علمي':
        user_state.secondary_type = 'علمي'
        user_states[message.chat.id] = user_state
        subjects = list(secondary_scores.keys())
        markup = create_subjects_markup(subjects)
        bot_ms.send_message(message.chat.id, "اختر المادة:", reply_markup=markup)

    elif message.text == 'ثانوية أدبي':
        user_state.secondary_type = 'أدبي'
        user_states[message.chat.id] = user_state
        subjects = list(secondary_scores_ad.keys())
        markup = create_subjects_markup(subjects)
        bot_ms.send_message(message.chat.id, "اختر المادة:", reply_markup=markup)

    elif message.text in list(preparatory_scores.keys()) + list(secondary_scores.keys()) + list(secondary_scores_ad.keys()):
        user_state.subject = message.text
        user_state.score_ratio = None
        user_states[message.chat.id] = user_state
        bot_ms.send_message(message.chat.id, f"*أرسل لي إجمالي عدد الأسئلة لـ {user_state.subject}\n يعنى عدد الاسئلة الي جاتك في الامتحان\n (60 او 56 او 48)*", parse_mode='Markdown')

    elif message.text.isdigit():
        if user_state and user_state.subject:
            if user_state.score_ratio is None:
                # مرحلة إدخال إجمالي عدد الأسئلة
                total_questions = int(message.text)
                if user_state.level == 'شهادة اعدادية':
                    score_key = preparatory_scores
                elif user_state.level  == 'علمي':
                    score_key = secondary_scores
                elif user_state.level == 'أدبي':
                    score_key = secondary_scores_ad
                else:
                    score_key = {}

                user_state.key_finale = score_key.get(user_state.subject, 1)
                
                user_state.score_ratio = user_state.key_finale / total_questions
                bot_ms.send_message(message.chat.id, f"*أرسل لي عدد الأسئلة الي حليتهن صح لـ {user_state.subject}*", parse_mode='Markdown')
            else:
                # مرحلة إدخال عدد الأسئلة المحلولة
                solved_questions = int(message.text)
                final_score = (solved_questions * user_state.score_ratio)
                final1 = round(user_state.score_ratio)
                final2 = round((final_score / user_state.score_ratio), 2)
                bot_ms.send_message(message.chat.id, f"*درجة السؤال {final1}،\n الناتج لـ {user_state.subject} هو: {final_score:.2f}\n النسبة المئوية للمادة: {final2}%*", parse_mode='Markdown')
                user_states[message.chat.id] = UserState()  # إعادة تعيين حالة المستخدم
    else:
        
        if text == message.text:
            massge(text,message)
            

def massge(text,message) :
    ref = db.reference(f'/reply/')
    data = ref.get()
    for message1 in data:
        ref = db.reference(f'/reply/{message1}')
        message_data = ref.get()
        for key , Value in message_data.items():
            if text == key:
                print(f"{text} : "+Value)
                bot_ms.send_message(message.from_user.id,f"*{Value}*",parse_mode='Markdown')  

@bot_ms.callback_query_handler(func=lambda call: call.data in ["thanoe_al"])
def callback_query1(call):
        chat_id = call.message.chat.id
        message_id=call.message.message_id
        if len(edit) > 0:
            message_id0 = edit[0]
        else:
            message_id0 = message_id
        if call.data == "thanoe_al":
                keyboard = telebot.types.InlineKeyboardMarkup()
                btn1 = telebot.types.InlineKeyboardButton(text='ثانوي علمي', callback_data='thanoe')
                btn2 = telebot.types.InlineKeyboardButton(text='ثانوي ادبي', callback_data='thanoe_ad')
                keyboard.add(btn1, btn2)
                msg = bot_ms.edit_message_text(chat_id=chat_id, message_id= message_id0 ,text= "حدد مستواك التعليمي", reply_markup=keyboard)
                last_message.clear()
                last_message[chat_id] = msg.message_id
                edit.clear()
                edit.append(msg.message_id)

@bot_ms.callback_query_handler(func=lambda call: call.data in ["thanoe", "adade",'thanoe_ad'])
def callback_query(call):
    global exam_type, student_ids,chat_id
    chat_id = call.message.chat.id
    message_id=call.message.message_id
    edit.append(message_id)
    exam_type[chat_id] = call.data
    if check_user_registration(chat_id):
        start_grades_input(chat_id)
    else:
        msg =  bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id , text="يرجى إرسال رقم الجلوس الخاص بك:")
        bot_ms.register_next_step_handler(msg, register_user)
        last_message[chat_id] = call.message.message_id
def enter_seat_number(message):
    global delettt
    code = message.text
    user_id = message.from_user.id
    if code:
        try:
            ref = db.reference(f'/codes/')
            data = ref.get()
            scode = None  # تعريف scode هنا لضمان أن تكون متاحة بعد الحلقة
            for scode in data:
                if scode == code:
                    break
        except Exception as e:
                pass
        if code == '/edit_id':
            return
        elif code == '/stop':
               حذف = bot_ms.reply_to(message,"تم ايقاف البوت")
               time.sleep(0.2)
               bot_ms.delete_message(user_id,message_id=حذف.message_id)
               return
        if scode == code:
            deltr = bot_ms.reply_to(message, "الكود صحيح ✅")
            user_ref = db.reference(f'users/{user_id}')
            message_id = deltr.message_id
            bot_ms.delete_message(user_id,int(delettt[0]))
            # حذف المستخدم
            user_ref.delete()
            ref.delete()
            time.sleep(2.3)
            msg = bot_ms.edit_message_text(chat_id=user_id, message_id=message_id, text="يرجى إرسال رقم الجلوس الخاص بك:")
            delettt.clear()
            bot_ms.register_next_step_handler(msg, register_user_code)
            delettt.append(msg.message_id)

        else:
            msg = bot_ms.reply_to(message, "الكود غير صحيح الرجاء ادخال كود صحيح : ")
            bot_ms.register_next_step_handler(msg, enter_seat_number)
def register_user_code(message):
    global user_id, seat_number, username, full_name, user_data
    user_id = message.from_user.id
    chat_id = user_id
    seat_number = message.text.strip()
    username = message.from_user.username
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}".strip()

    if seat_number.isdigit() and len(seat_number) == 6 and 100000 <= int(seat_number) <= 700000:
        # تحقق من وجود رقم الجلوس مسبقًا
        seat_ref = db.reference('/users').order_by_child('seat_number').equal_to(seat_number).get()

        if seat_ref:
            # التأكد من عدم إرسال التحذير مرتين
            if not hasattr(message, 'already_warned') or not message.already_warned:
                msg = bot_ms.send_message(user_id, "رقم الجلوس موجود بالفعل. الرجاء إدخال رقم جلوس آخر: ")
                bot_ms.register_next_step_handler(msg, register_user_code)
                message.already_warned = True  # وضع علامة على أنه تم تحذير المستخدم بالفعل
            return
        user_data = f"اسم المستخدم: {full_name}\nيوزره: @{username}\nمعرف المستخدم: {user_id}\nرقم الجلوس: {seat_number}\n\n"
        # تخزين بيانات المستخدم
        db.reference(f'/users/{user_id}').set({
            'full_name': full_name,
            'username': username,
            'seat_number': seat_number,
            'created_at': created_at
        })

        # إرسال رسالة النجاح
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        btn_ky = telebot.types.InlineKeyboardButton(text='عرض البيانات', callback_data='view_text1')
        keyboard1.add(btn_ky)
        key_bord = bot_ms.send_message(chat_id, "*تم تسجيل بياناتك بنجاح:*", parse_mode='Markdown', reply_markup=keyboard1)

        # حذف الرسالة القديمة إذا كانت موجودة
        if delettt:
            bot_ms.delete_message(user_id, delettt[0])
            delettt.clear()

    else:
        msg = bot_ms.send_message(user_id, "رقم الجلوس غير صالح. الرجاء إدخال رقم جلوس صحيح: ")
        bot_ms.register_next_step_handler(msg, register_user_code)


def register_user(message):
    global user_id,seat_number,username,full_name, user_data
    user_id = message.from_user.id
    chat_id = user_id
    seat_number = message.text.strip()
    username = message.from_user.username
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}".strip()

    if seat_number.isdigit() and len(seat_number) == 6 and 100000 <= int(seat_number) <= 700000:
        # تحقق من وجود رقم الجلوس مسبقًا
        seat_ref = db.reference('/users').order_by_child('seat_number').equal_to(seat_number).get()

        if seat_ref:
            msg = bot_ms.send_message(user_id, "رقم الجلوس موجود بالفعل. الرجاء إدخال رقم جلوس آخر: ")
            bot_ms.register_next_step_handler(msg, register_user)
            return

        user_data = f"اسم المستخدم: {full_name}\nيوزره: @{username}\nمعرف المستخدم: {user_id}\nرقم الجلوس: {seat_number}\n\n"

        # تخزين بيانات المستخدم
        db.reference(f'/users/{user_id}').set({
            'full_name': full_name,
            'username': username,
            'seat_number': seat_number,
            'created_at': created_at
        })
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        btn_ky = telebot.types.InlineKeyboardButton(text='عرض البيانات', callback_data='view_text')
        keyboard1.add(btn_ky)
        key_bord = bot_ms.send_message(chat_id, f"*تم تسجيل بياناتك بنجاح:*",parse_mode='Markdown', reply_markup=keyboard1)
        delet.append(key_bord.message_id)
    else:
        msg = bot_ms.send_message(chat_id, "الرجاء إدخال رقم جلوس صحيح : ")
        bot_ms.register_next_step_handler(msg, register_user)



@bot_ms.callback_query_handler(func=lambda call: call.data in ["notify_admin_yes", "notify_admin_no","thanoe1", "adade1","thanoe_alm","thanoe_ady"])
def handle_admin_notify(call):
    if not is_bot_running:
        return

    chat_id = call.message.chat.id
    if call.data == "thanoe1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='ثانوي علمي', callback_data='thanoe_alm')
        btn2 = telebot.types.InlineKeyboardButton(text='ثانوي ادبي', callback_data='thanoe_ady')
        keyboard.add(btn1, btn2)
        msg = bot_ms.edit_message_text(chat_id=chat_id, message_id = call.message.message_id  ,text= "حدد مستواك التعليمي", reply_markup=keyboard)
        return
    elif call.data == "adade1":
        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="""*شرط النجاح لكل مادة من المواد الاتيه هو :

- التربية الإسلامية = 40
- النحو والقراءة والنصوص = 80
- الكتابة = 40
- اللغة الإنجليزية = 80
- الحاسوب = 40
- الرياضيات = 100
- العلوم = 100
- التاريخ = 40
- الجغرافيا = 40*""", parse_mode='Markdown')
        return
    elif call.data == "thanoe_alm":
       bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="""*شرط النجاح لكل مادة من المواد الاتيه هو :

- التربية الإسلامية = 40
- اللغة العربية = 80
- اللغة الإنجليزية = 80
- تقنية معلومات = 40
- الرياضيات = 100
- الاحصاء = 40
- الفيزياء = 100
- الكيمياء = 80
- الاحياء = 80*""", parse_mode='Markdown')
       return
    elif call.data == "thanoe_ady":
       bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="""*شرط النجاح لكل مادة من المواد الاتيه هو :

- التربية الإسلامية = 40
- اللغة العربية = 140
- اللغة الإنجليزية = 100
- تقنية معلومات = 40
- الإحصاء = 40
- التاريخ = 60
- الجغرافيا = 60
- الفلسفة = 60
- علم الاجتماع = 40
- علم النفس = 40*""", parse_mode='Markdown')
       return
    if call.data == "notify_admin_yes":
        full_name = f"{call.from_user.first_name} {call.from_user.last_name}" if call.from_user.last_name else call.from_user.first_name
        user_id = call.from_user.id
        username = f"@{call.from_user.username}" if call.from_user.username else "بدون يوزر"

        if not admin_chat_id:
            bot_ms.send_message(chat_id, "حدث خطأ: لم يتم تعيين معرف الأدمن.")
            return

        bot_ms.send_message(admin_chat_id, f"هذا الشخص استدعاك للمحادثة:\nالاسم: {full_name}\nاليوزر: {username}\nID: {user_id}")

        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم إعلام الأدمن. سيتم التواصل معك قريباً.")
    else:
        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم إلغاء الإشعار.")
def sned_all_user(message):
    sand_all = message.text
    if sand_all == '/stop':
        return
    ref = db.reference(f'/users_all/')
    data = ref.get()
    for sned in data:
        bot_ms.send_message(sned,f'*{sand_all}*',parse_mode='Markdown')



@bot_ms.callback_query_handler(func=lambda call: call.data in ["create_new_code" ,'view_text',"byant1","byant2","view_text1","rep_end","fos","ter"])
def create_code_callback(call):
    global edite 
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_yes1 = telebot.types.InlineKeyboardButton(text='نعم', callback_data='byant1')
    btn_yes2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='byant2')
    keyboard.add(btn_yes1,btn_yes2)
    chat_id = call.from_user.id
    if call.data == "view_text":
        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"{user_data}")
        bot_ms.send_chat_action(call.from_user.id, "typing")
        message_id=call.message.message_id
        delet.append(message_id)
        time.sleep(3)
        bot_ms.send_message(call.from_user.id, "*هـل تـريـد الـبـدا*", reply_markup=keyboard,parse_mode='Markdown')
    elif call.data == "ter":
        db.reference(f'/reply/{reply_ms[2]}').set({
                 reply_ms[0] : reply_ms[1],
                'created_at': created_at
                })
        bot_ms.edit_message_text(chat_id=chat_id, message_id=reply_ms[3], text=f"تم اضافة الرد في مجموعة : {reply_ms[2]}")
        reply_ms.clear()
    elif call.data == "fos":
        bot_ms.delete_message(chat_id,reply_ms[3])
        reply_ms.clear()
        pass
    elif call.data == "view_text1":
          bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"{user_data}")
    elif call.data == "rep_end":
        mas = bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="الرجاء ادخال الرسالة الاساسية لي يتم الرد عليها :")
        bot_ms.register_next_step_handler(mas,massege_Ass)
    elif call.data == "byant1":
        edite = False
        bot_ms.send_chat_action(call.from_user.id, "typing")
        time.sleep(0.25)
        mssgse_id = delet[0]
        delet.clear()
        bot_ms.delete_message(chat_id,mssgse_id)
        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="الأن سوف نـبـدا بي ادخال الدرجات :")
        message_id = call.message.message_id
        edit.append(message_id)
        bot_ms.send_chat_action(call.from_user.id, "typing")
        time.sleep(0.25)
        start_grades_input(chat_id)
    elif call.data == "byant2":
        bot_ms.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم الايقاف")
        message_id=call.message.message_id
        delet2.append(message_id)
        time.sleep(2)
        bot_ms.delete_message(chat_id,delet[0])
        time.sleep(2)
        bot_ms.delete_message(chat_id,delet2[0])
        delet.clear()
        delet2.clear()
    elif call.data == "create_new_code":
        if (call.message.chat.id) == admin_chat_id:
            code = generate_random_code()  # توليد كود عشوائي
            db.reference(f'/codes/{code}').set({
                'created_by': admin_chat_id,
                'used_by': None,
                'created_at': created_at
                })
            bot_ms.answer_callback_query(call.id, f"تم إنشاء الكود: {code}")
            bot_ms.send_message(call.message.chat.id, f"تم إنشاء الكود: `{code}`",parse_mode='Markdown')
        else:
            bot_ms.answer_callback_query(call.id, "ليس لديك صلاحية للقيام بهذا الإجراء.")

def massege_Ass(message):
    masge_Ass = message.text
    coun = 0
    if masge_Ass == '/stop':
        return
    ref = db.reference(f'/reply/')
    data = ref.get()
    while True:
        for red in data:
            ref = db.reference(f'/reply/{red}')
            red_data = ref.get()
            for key in red_data:
                print(key)
                if masge_Ass == key:
                    mes = bot_ms.send_message(message.from_user.id,f"*عذرا، هذا الرسالة محفوظة الرجاء ادخال رسالة اخره او اكتب امر /stop\n الرسالة موجوده هنا  :{red} *", parse_mode='Markdown')
                    bot_ms.register_next_step_handler(mes,massege_Ass)
                    return
                elif key  == "created_at":
                    pass
        
        mes1 = bot_ms.send_message(message.from_user.id,"الرجاء ادخال الرد ليتم اضافته : ")
        reply_ms.append(masge_Ass) #0
        bot_ms.register_next_step_handler(mes1,massege_red)
        return        
    
def massege_red(message):
    coun = 1
    global reply_ms
    massege_red = message.text
    ref = db.reference(f'/reply/')
    data = ref.get()
    while True:
        for red in data:
            if red == f'red : {coun}':
                coun+=1
            else:
                name = f'red : {coun}'
                print(name)
                keyboard = telebot.types.InlineKeyboardMarkup()
                btn_yes = telebot.types.InlineKeyboardButton(text='موفق ❤️ ', callback_data='ter')
                btn_yes2 = telebot.types.InlineKeyboardButton(text='غير موفق ❌', callback_data='fos')
                keyboard.add(btn_yes,btn_yes2)
                msx = bot_ms.send_message(message.from_user.id,f"*هل انت موفق على رفع هذا :\n الرسالة : \n {reply_ms[0]} \n الرد : \n {massege_red} *",reply_markup=keyboard, parse_mode='Markdown')
                reply_ms.append(massege_red) #1
                reply_ms.append(name) #2
                reply_ms.append(msx.message_id) #3
                return
        
    
        

# التحقق من الكود وإتاحة التعديل
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

def search_user_by_id(message):
    user_identifier = message.text.strip()  # يمكن أن يكون ID أو username
    user_id = message.from_user.id
    ref = db.reference(f'/users/')
    data = ref.get()
    contre = 0
    for scode in data :
        contre += 1
        if scode == user_identifier:
            ref = db.reference(f'/users/{user_identifier}')
            data = ref.get()
            datax = ''
            for keys, valuse in data.items():
                datax= f'{keys} : {valuse}'+' \n'+datax
            datax = f'بيانات المستخدم {user_identifier}\n مكانه في قاعدة البيانات  : ({contre}) \n'+datax
            bot_ms.send_message(admin_chat_id,f'*{datax}*',parse_mode='Markdown')
            break

def send_message_to_all_users(message_text):
    users_ref = db.reference('/users')
    users = users_ref.get()  # استرجاع جميع بيانات المستخدمين
    if users:
        for user_id in users.keys():
            try:
                bot_ms.send_message(user_id, message_text)
            except Exception as e:
                print(f"Error sending message to user {user_id}: {e}")
def check_subscription(chat_id):
    for channel in channels:
        try:
            member_status = bot_ms.get_chat_member(channel, chat_id).status
            if member_status in ['left', 'restricted', 'kicked']:
                return False
        except Exception as e:
            print(f"Error checking subscription for {chat_id} in {channel}: {e}")
            return False
    return True

def send_subscription_message(chat_id):
    myMarkup = telebot.types.InlineKeyboardMarkup()
    for channel in channels:
        try:
            my_chat = bot_ms.get_chat(channel)
            myMarkup.add(telebot.types.InlineKeyboardButton(text=my_chat.title, url=my_chat.invite_link))
        except Exception as e:
            print(f"Error getting chat info for {channel}: {e}")

    bot_ms.send_message(
        chat_id,
        "عزيزي، يجب عليك الاشتراك في جميع القنوات التالية لاستخدام البوت:",
        reply_markup=myMarkup
    )

def start_grades_input(chat_id):
    global current_step, user_scores, user_work_scores,edit,edite
    message_id = edit[0]
    user_scores[chat_id] = {}
    user_work_scores[chat_id] = {}
    current_step[chat_id] = 1
    if exam_type[chat_id] == "thanoe":
            try:
                if not edite == True:
                    edite = True
                    message_id1 = edit[2]
                    
                    bot_ms.edit_message_text(chat_id=chat_id, message_id= message_id1 ,text= thanoe[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
            
            
                else :
                    bot_ms.edit_message_text(chat_id=chat_id, message_id= message_id ,text= thanoe[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
                
            except Exception as e:
             error_message = f"هناك خطاء غير متوقع الرجاء التوصل مع الادمن لي اصلحه : {e}"
             bot_ms.send_message(admin_chat_id, error_message)
    elif exam_type[chat_id] == "thanoe_ad":
        try:
                if not edite == True:
                    message_id1 = edit[2]
                    
                    edite = True
                    bot_ms.edit_message_text(chat_id=chat_id, message_id= message_id1 ,text= thanoe_ad[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
            
            
                else :
                    bot_ms.edit_message_text(chat_id=chat_id, message_id= message_id ,text= thanoe_ad[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
                
        except Exception as e:
             error_message = f"هناك خطاء غير متوقع الرجاء التوصل مع الادمن لي اصلحه : {e}"
             bot_ms.send_message(admin_chat_id, error_message)

    else:
            try:

                if not edite == True:
                    edite = True
                    message_id1 = edit[2]
                    
                    bot_ms.edit_message_text(chat_id=chat_id, message_id=message_id1, text=adade[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
                

                else:
                    bot_ms.edit_message_text(chat_id=chat_id, message_id=message_id, text=adade[1], parse_mode='Markdown')
                    bot_ms.register_next_step_handler_by_chat_id(chat_id, process_exam_score)
                    edit.clear()
                
            except Exception as e:
             error_message = f"هناك خطاء غير متوقع الرجاء التوصل مع الادمن لي اصلحه : {e}"
             bot_ms.send_message(admin_chat_id, error_message) 

def process_exam_score(message):
    
    global current_step, user_scores, exam_type
    chat_id = message.chat.id
    score = message.text.strip()
    bot_ms.send_chat_action(message.from_user.id, "typing")
    time.sleep(0.25)    
    
    if str(score)=='/stop':
        user_scores.clear() 
        user_work_scores.clear()
        حذف = bot_ms.reply_to(message,"تم ايقاف البوت")
        time.sleep(0.2)
        bot_ms.delete_message(chat_id,message_id=حذف.message_id)
        return
    elif str(score)=='/math':
        user_scores.clear() 
        user_work_scores.clear()
        حذف = bot_ms.reply_to(message,"تم ايقاف البوت")
        time.sleep(0.2)
        bot_ms.delete_message(chat_id,message_id=حذف.message_id)
        return
    else:
       if not score.isdigit():
        bot_ms.send_chat_action(message.from_user.id, "typing")
        time.sleep(0.15)
        bot_ms.send_message(chat_id, "يرجى إدخال رقم صحيح.")
        bot_ms.register_next_step_handler(message, process_exam_score)
        return 
    

    current_subject = current_step[chat_id]

    user_scores[chat_id][current_subject] = int(score)

    if exam_type[chat_id] == "thanoe":
        bot_ms.send_chat_action(message.from_user.id, "typing")
        if current_subject < len(thanoe):
            bot_ms.send_message(chat_id, thanoe_work[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)
        else:
            bot_ms.send_message(chat_id, thanoe_work[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)
    elif exam_type[chat_id] == "thanoe_ad":
        bot_ms.send_chat_action(message.from_user.id, "typing")
        if current_subject < len(thanoe_ad):
            bot_ms.send_message(chat_id, thanoe_work_ad[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)
        else:
            bot_ms.send_message(chat_id, thanoe_work_ad[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)        

    else:
        if current_subject < len(adade):
            bot_ms.send_message(chat_id, adade_work[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)
        else:
            bot_ms.send_message(chat_id, adade_work[current_subject], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_work_score)

def process_work_score(message):
    
    global current_step, user_work_scores, exam_type, thanoe, adade, thanoe_work, adade_work
    chat_id = message.chat.id
    score = message.text.strip()
    bot_ms.send_chat_action(message.from_user.id, "typing")
    time.sleep(0.15)
    if str(score)=='/stop':
        user_scores.clear() 
        user_work_scores.clear()
        حذف = bot_ms.reply_to(message,"تم ايقاف البوت")
        time.sleep(0.2)
        bot_ms.delete_message(chat_id,message_id=حذف.message_id)
        return
    elif str(score)=='/math':
        user_scores.clear() 
        user_work_scores.clear()
        حذف = bot_ms.reply_to(message,"تم ايقاف البوت")
        time.sleep(0.2)
        bot_ms.delete_message(chat_id,message_id=حذف.message_id)
        return
    else: 
        if not score.isdigit():
            bot_ms.send_chat_action(message.from_user.id, "typing")
            time.sleep(0.25)
            bot_ms.send_message(chat_id, "يرجى إدخال رقم صحيح.")
            bot_ms.register_next_step_handler(message, process_work_score)
            return

    current_subject = current_step[chat_id]
    user_work_scores[chat_id][current_subject] = int(score)

    # تحقق من نوع الامتحان
    if exam_type[chat_id] == "thanoe":
        bot_ms.send_chat_action(message.from_user.id, "typing")
        # الانتقال إلى المادة التالية
        current_step[chat_id] += 1
        if current_step[chat_id] <= len(thanoe):
            bot_ms.send_message(chat_id, thanoe[current_step[chat_id]], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_exam_score)
        else:
            calculate_results(chat_id)
    elif exam_type[chat_id] == "thanoe_ad":
        bot_ms.send_chat_action(message.from_user.id, "typing")
        # الانتقال إلى المادة التالية
        current_step[chat_id] += 1
        if current_step[chat_id] <= len(thanoe_ad):
            bot_ms.send_message(chat_id, thanoe_ad[current_step[chat_id]], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_exam_score)
        else:
            calculate_results(chat_id)        
    else:
        # الانتقال إلى المادة التالية
        current_step[chat_id] += 1
        if current_step[chat_id] <= len(adade):
            bot_ms.send_message(chat_id, adade[current_step[chat_id]], parse_mode='Markdown')
            bot_ms.register_next_step_handler(message, process_exam_score)
        else:
            calculate_results(chat_id)
def calculate_results(chat_id):
    global user_scores, user_work_scores, exam_type, thanoe_min_scores,thanoe_min_scores_ad, adade_min_scores, total_new, المادة
    
    total_new = 0 ; المادة = ""
    if exam_type[chat_id] == "thanoe":
        total_marks = 640
        exam_subjects = thanoe_exam
        min_scores = thanoe_min_scores
        min_scor = secondary_scores
    elif exam_type[chat_id] == "thanoe_ad":
        total_marks = 620
        exam_subjects = thanoe_exam_ad
        min_scores = thanoe_min_scores_ad
        min_scor = secondary_scores_ad

    else:
        total_marks = 560
        exam_subjects = adade_exam
        min_scores = adade_min_scores
        min_scor = preparatory_scores

    total_score = 0
    passed_all = True
    gred.clear()
    for subject_id in range(1, len(exam_subjects) + 1):
        if subject_id in user_scores[chat_id] and subject_id in user_work_scores[chat_id]:
            exam_score = user_scores[chat_id][subject_id]
            work_score = user_work_scores[chat_id][subject_id]
            total_subject_score = (exam_score + work_score)/2
            total_subject_score1 = (exam_score + work_score)
            aln = min_scor.get(exam_subjects.get(subject_id))/2
            print(f"{exam_subjects.get(subject_id)} : {exam_score} > {aln} ")
            if exam_score < (min_scor.get(exam_subjects.get(subject_id))/2) :
                total_new = total_new + (total_subject_score1 /2)
                gred.append(exam_subjects[subject_id])
                passed_all = False    
            else:
                total_score += total_subject_score
        else:
            bot_ms.send_message(chat_id, f"لم يتم إدخال درجات مادة {exam_subjects[subject_id]} بشكل كامل.")
            passed_all = False
            break
    if not passed_all:
                        if gred:
                            if len(gred) == 1:
                                bot_ms.send_message(chat_id, f"عذرًا، لقد رسبت في مادة {gred[0]}❤️،\n لأنك لم تستوفِ شرط النجاح في المادة،\n اكتب او انقر على النص للنسخ \" `شرط النجاح` \" ليظهر لك شروط النجاح في المادة.", parse_mode='Markdown')
                            else:
                                failed_subjects_str = "، ".join(gred)
                                bot_ms.send_message(chat_id, f"عذرًا، لقد رسبت في المواد التالية: {failed_subjects_str} ❤️.\n لأنك لم تستوفِ شرط النجاح في هذه المواد،\n اكتب او انقر على النص للنسخ  \" `شرط النجاح` \" ليظهر لك شروط النجاح في المواد.",parse_mode='Markdown')
                            
            
    if passed_all:
        percentage = (total_score / total_marks) * 100

        if percentage >= 85:
            grade = "ممتاز"
        elif percentage >= 76:
            grade = "جيد جداً"
        elif percentage >= 65:
            grade = "جيد"
        elif percentage >= 50:
            grade = "مقبول"
        else:
            grade = "راسب"

        bot_ms.send_message(chat_id, f"*النسبة المئوية الخاصة بك هي: {percentage:.2f}%\nالتقدير: {grade}*",parse_mode='Markdown')
    else:
        total_score2 = total_score + total_new
        percent = (round(((total_score2/total_marks)*100),2))
        
        if percent >= 85:
            grade = "ممتاز"
        elif percent >= 76:
            grade = "جيد جداً"
        elif percent >= 65:
            grade = "جيد"
        elif percent >= 50:
            grade = "مقبول"
        else:
            grade = "راسب"      
        bot_ms.send_message(chat_id, f"*سنقوم بحساب النتيجة بناءً على الدرجات المتوفرة.\n النسبة المئوية الخاصة بك هي : {percent:.2f}%\n التقدير: {grade}*",parse_mode='Markdown')
        gred.clear()
        
    # إعادة تعيين المتغيرات
    del user_scores[chat_id]
    del user_work_scores[chat_id]
    del current_step[chat_id]

def handle_command(message):
    user_comment = message.text

    # التحقق من أن النص ليس أمرًا (يبدأ بـ "/")
    if user_comment.startswith('/'):
        return

    user_info = f"الاسم: {message.from_user.first_name}\nيوزر: @{message.from_user.username}\nID: {message.from_user.id}"

    # إرسال التعليق للأدمن
    bot_ms.send_message(admin_chat_id, f"لقد قام هذا الشخص بإرسال تعليق:\n{user_info}\n\nالتعليق:\n{user_comment}")

    # تأكيد الإرسال للمستخدم
    bot_ms.send_message(message.chat.id, "لقد تم إرسال تعليقك. شكرًا لك! هذه سوف يحسن من اداء البوت 👨‍💻🤍")


def create_subjects_markup(subjects):
    # تنظيم الأزرار في ثلاثة أعمدة
    markup = ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    for subject in subjects:
        markup.add(KeyboardButton(subject))
    return markup
def send_levels(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(KeyboardButton('شهادة اعدادية'), KeyboardButton('شهادة ثانوية'))
    bot_ms.send_message(message.chat.id, "حدد مستواك التعليمي:", reply_markup=markup)
    user_states[message.chat.id] = UserState()  # إعداد الحالة للمستخدم
def get_user_seat_number(user_id):
    global seat_number
    # جلب مرجع لبيانات المستخدم بناءً على معرف المستخدم
    ref = db.reference(f'/users/{user_id}')
    user_data = ref.get()

    # التحقق من وجود بيانات للمستخدم
    if user_data:
        seat_number = user_data.get('seat_number')
        if seat_number:
            return seat_number
        else:
            return "رقم الجلوس غير متوفر لهذا المستخدم."
    else:
        return "لم يتم العثور على المستخدم."

bot_ms.infinity_polling()