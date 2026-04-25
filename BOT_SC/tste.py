from telebot import TeleBot
import requests
import json

# استبدل بـ التوكن الخاص بالبوت
bot = TeleBot(token="7339244017:AAHRTaoEgMTjpeQ10Q41-5XjRt3DDodUqDI")

# الرؤوس المستخدمة في طلب الـ API الخارجي
headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Length': '25',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# عند ارسال المستخدم /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, f'• مرحبا بك {message.from_user.first_name}!\n\n'
                          f'• انا بوت يساعدك في معرفة وقت إنشاء حسابك على تليجرام.\n'
                          f'• رجاءً أرسل معرف حسابك (ID)')

# معالجة المعرفات التي يرسلها المستخدم
@bot.message_handler(func=lambda message: True)
def process_user_id(message):
    try:
        # تحويل النص إلى رقم (ID)
        user_id = int(message.text)
    except ValueError:
        bot.reply_to(message, '• رجاءً أرسل معرف حسابك بشكل صحيح (يجب أن يكون رقمًا)')
        return

    # البيانات التي يتم إرسالها إلى الخدمة
    payload = json.dumps({"telegramId": user_id})
    
    try:
        # إرسال الطلب إلى الخدمة الخارجية
        response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=payload)
        # التحقق من حالة الرد
        if response.status_code == 200:
            # قراءة البيانات بصيغة JSON
            data = response.json()
            print(data)
            # التحقق من وجود البيانات المطلوبة
            if 'data' in data and 'date' in data['data']:
                account_creation_date = data['data']['date']

                # صياغة الرد لعرض التاريخ
                bot.reply_to(message, f'• تاريخ إنشاء حسابك على تليجرام هو: {account_creation_date}')
            else:
                # عرض أي بيانات إضافية في حال وجود خطأ أو غياب التاريخ
                bot.reply_to(message, '• لم أتمكن من الحصول على تاريخ إنشاء الحساب، رجاءً تحقق من معرفك.')
        else:
            bot.reply_to(message, '• حدث خطأ في الخدمة الخارجية، حاول مرة أخرى لاحقًا.')

    except requests.exceptions.RequestException as e:
        # معالجة الأخطاء المتعلقة بالشبكة أو الخدمة
        bot.reply_to(message, f'• حدث خطأ أثناء الاتصال بالخدمة الخارجية: {str(e)}')

# بدء تشغيل البوت
bot.infinity_polling()