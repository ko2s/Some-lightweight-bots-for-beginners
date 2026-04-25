from def_main import *
@bot.message_handler(commands=["start","help","id",'kick', 'ban', 'unban', 'mute', 'unmute',"info","warn","lock","unlock","rules","members"])
def handle_user(message):
    user = message.from_user
    chat_id = user.id
    first_name = user.first_name or "بدون اسم اول"
    last_name = user.last_name or "بدون اسم ثاني"
    full_name = f"{first_name} {last_name}".strip()
    username = user.username or "بدون يوزر"
    language = user.language_code
    is_bot = user.is_bot
    ref = db.reference(f'/users/{chat_id}')
    data = ref.get()

    is_admin = admin_chat.admin_start(chat_id)
    tset = SARCH_USER(chat_id)

    try:
        # التحقق من وجود المستخدم في قاعدة البيانات
        if data is None:
            add_new_user(chat_id, full_name, username, language, is_bot)
            send_welcome_message(chat_id, message)
        else:
            if message.chat.type == "private":
                handle_existing_user(chat_id, message, is_admin, full_name)
            elif message.chat.type in ["group","supergroup"]:
                manage_members(message)

    except Exception as e:
        print(f"Error: {e}")
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    handle_all_messages1(message)


@bot.message_handler(content_types=[photo,voice,audio,document,sticker,video,video_note,location,contact])
def lock (message):
    chat_id = message.chat.id
    #هنا نقدر نضبف شرط بحيث يقدر يمنع الصور من القروب بروحه ومن الخاص بروحه
    if message.content_type in op_close and message.chat.type == "private":
        if not op_close.get(message.content_type) == "None":
            bot.delete_message(message.chat.id, message.message_id)
    #هنا يتأكد من ان الصورة جايه من خاص شخص
    if message.content_type == 'photo' and message.chat.type == "private":
        #pytesseract.pytesseract.tesseract_cmd = r'E:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        photo2 = message.photo
        #هنا يتأكد من ان جايته صوره
        if photo2:
            #اختصارات كل شىء في دوال لي تسهيل التعامل مع الكود
            process_photo(message, chat_id)
@bot.my_chat_member_handler()
def handle_new_member(message):
    global Enter_add_info
    group_id = int(message.chat.id)
    user_id = int(message.from_user.id)
    bot_user = bot.get_me()
    admin_chat = bot.get_chat(admin[0])
    super_ts = []
    admin_ids = []
    print(Enter_add_info)
    # تحقق من حالة البوت في المجموعة
    try:
        bot_member = bot.get_chat_member(group_id, bot_user.id)
        if bot_member.status in ["kicked", "left"]:
            return
    except:
        return

    # تحقق من نوع المجموعة
    chat_type = message.chat.type
    if chat_type == "channel":
        bot.leave_chat(group_id)
        return

    # جلب قائمة الإداريين
    if chat_type in ["supergroup", "group"]:
        try:
            chat_admins = bot.get_chat_administrators(group_id)
            admin_ids = [admin.user.id for admin in chat_admins]
        except:
            pass

    # جلب بيانات من قاعدة البيانات
    ref = db.reference('/SuperTS')
    data_supervisors = ref.get() or []
    ref = db.reference('/Supervisor')
    data_groups = ref.get() or {}

    if data_supervisors:
        for user in data_supervisors:
            if int(user) == user_id:
                super_ts.append(int(user))

    # تحقق إذا كان المستخدم مشرفًا في البوت
    if bot_member.status in ["administrator", "creator"]:
        if user_id in super_ts or user_id == admin[0]:
            handle_admin_user(group_id, user_id, data_groups)
        else:
            send_and_leave(group_id, user_id, f"عذرًا، لا يمكنك استخدام البوت إلا بتعيينك مشرفًا في البوت من قبل أدمن البوت @{admin_chat.username}👨‍💻✅")
    else:
        handle_non_admin_user(group_id, user_id, admin_ids, super_ts, admin_chat)

def handle_admin_user(group_id, user_id, data_groups):
    if Enter_add_info[0] == True:
        Enter_add_info.clear()
        # التحقق من وجود المجموعة في قاعدة البيانات
        if str(group_id) in data_groups:
            ref = db.reference(f'/Supervisor/{group_id}')
            group_data = ref.get()
            if group_data and "subject" in group_data:
                bot.send_message(user_id, f"تم إضافة المادة مسبقًا رقم المادة: {group_data['subject']}")
                return
        Group_idE.clear()
        if group_id not in Group_idE and user_id not in Group_idE:
            Group_idE.append(group_id)#0
            Group_idE.append(user_id)#1
            

        # إرسال الأقسام إذا كانت المجموعة غير موجودة
        keyboard = InlineKeyboardMarkup()
        for department in college_departments:
            keyboard.add(InlineKeyboardButton(text=f'{department}', callback_data=f'college_{department}'))

        bot.send_message(user_id, "تم إضافة البوت، وتم ترقيته أدمن✅\nالآن اختر أحد الأقسام", reply_markup=keyboard)

def handle_non_admin_user(group_id, user_id, admin_ids, super_ts, admin_chat):
    if not admin_ids:  # إذا لم يكن بالإمكان الوصول إلى قائمة الإداريين
        if user_id in super_ts or user_id == admin[0]:
            bot.send_message(user_id, "عذرًا، لا يمكن للبوت الوصول إلى قائمة المسؤولين لأنه يفتقد إلى صلاحية 'إدارة المجموعة'.\n\nيرجى منح البوت هذه الصلاحية من إعدادات المجموعة.")
            wait_for_admin_permission(group_id, user_id)
        else:
            send_and_leave(group_id, user_id, f"عذرًا، لا يمكنك استخدام البوت إلا بتعيينك مشرفًا في البوت من قبل أدمن البوت @{admin_chat.username}👨‍💻✅")
    else:
        if user_id not in admin_ids:
            send_and_leave(group_id, user_id, "عذرًا، أنت لست مشرفًا في هذه المجموعة ✅")
        elif user_id in admin_ids and user_id not in super_ts:
            send_and_leave(group_id, user_id, f"عذرًا، لا يمكنك استخدام البوت إلا بتعيينك مشرفًا في البوت من قبل أدمن البوت @{admin_chat.username}👨‍💻✅")

def wait_for_admin_permission(group_id, user_id):
    time.sleep(1800)  # الانتظار نصف ساعة
    bot_member = bot.get_chat_member(group_id, bot.get_me().id)
    if bot_member.status not in ["administrator", "creator"]:
        send_and_leave(group_id, user_id, "عذرًا، انتهى الوقت المحدد لترقية البوت أدمن 🕘")

def send_and_leave(group_id, user_id, message):
    try:
        bot.send_message(user_id, message)
        time.sleep(4)
        bot.leave_chat(group_id)
    except:
        pass
@bot.message_handler(content_types=['new_chat_members'])
def inf_grobe(message):
    #هذا ID المجموعة
    chat_id = message.chat.id
    #معلومات القروب
    chat = bot.get_chat(chat_id)
    #هنا يتأكد البوت انه ادمن او لا
    bot_member = bot.get_chat_member(chat_id,bot.get_me().id)
    if bot_member.status == "member":
        return

    ref = db.reference(f'/Student')
    data = ref.get()
    #استخراج ID المستخدم الجديد
    for new_member in message.new_chat_members:
        user_id = new_member.id
    #اذا كان المستخدم الي انضم الي القروب هو نفسه الادمن الرئيسي لا تفعل شىء
    if user_id == admin[0]:
        return
    if user_id:
        #هنا جلب معومات المستخدم
        user_info = bot.get_chat(user_id)
        #هنا اتأكد من ان الشخص الي انضاف مش البوت
        if user_id == bot.get_me().id:
            return
        #هنا اتـأكد من ان الي انضاف بوت او لا
        if message.from_user.is_bot:
            return
        #هنا تتأكد من ان الطالب موجود في قاعدة البانات ام لا
        if data is not None:
            for stu in data:
                if int(user_id) == int(stu):
                    bot.send_message(chat_id,f"نورات من جديد يا @{user_info.username if user_info.username else f"{user_info.first_name if user_info.first_name else "بدون اسم"} {user_info.last_name if user_info.last_name else ""}" } 🌹")
                    return
        try:
            if chat.type in ["supergroup", "group"]:
                # تحقق من صلاحيات البوت
                bot_member = bot.get_chat_member(chat_id, bot.get_me().id)
                if not bot_member.can_restrict_members:
                    bot.send_message(chat_id, "⚠️ لا أملك صلاحيات تقييد الأعضاء. يرجى منح البوت صلاحية إدارة المجموعة.")
                    return

                # تقييد العضو
                bot.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=False))
                user_name = user_info.username if user_info.username else f"{user_info.first_name or 'بدون اسم'} {user_info.last_name or ''}"
                bot.send_message(chat_id, f"⚠️ عذرًا [@{user_name}]، تم كتمك في المجموعة لفترة مؤقتة.\nإذا كنت من طلاب المادة، يمكنك التواصل مع هذا البوت لفك الكتم: @{bot.user.username} 🤖\n📌 ملاحظة: فترة الكتم هي ثلاثة أيام، وبعدها سيتم حظرك بشكل نهائي من المجموعة.")

                # إضافة العضو إلى قاعدة البيانات
                db.reference(f'/Bin/{chat_id}/{user_id}').set({
                    'created_at': created_at,
                })
                # تنفيذ حظر بعد 3 أيام
                threading.Thread(target=ban_after_duration, args=(chat_id, user_id, 259200)).start()
            else:
                bot.send_message(chat_id, "⚠️ مجموعتك عادية، ولا يمكن استخدام الميزات المتقدمة. يرجى تحويلها إلى سوبر جروب.")
        except Exception as e:
            bot.send_message(admin[0], f"فشل كتم هذا العضو: {e}")
#هنا يتم حظر المستخدم
def ban_after_duration(chat_id,user_id,duration):
    time.sleep(duration)
    bot.kick_chat_member(chat_id,user_id)
    ref = db.reference(f'/Bin/{user_id}').delete()
@bot.callback_query_handler(func= lambda call: call.data in (["photo_op","voice_op","audio_op","document_op","sticker_op","video_op","video_note_op","location_op","contact_op","photo_close","voice_close","audio_close","document_close","sticker_close","video_close","video_note_close","location_close","contact_close"]))
def callbacd(call):
    global photo,voice,audio,document,sticker,video,video_note,location,contact,op_close,mtargam
    close.clear()
    main_callbacd(call)
#;;;;;;
@bot.callback_query_handler(func= lambda call: call.data in ["no_send_admin","yas_send_admin",'admin_send_all',"stetes","viewa_tsoey","man_hoa","usere_adda","redback1","suggest_modification","check_speed","creas","sql_shb","report_issue","send_private_message","calculate_expression","create_qr","fetch_html","create_files","carha","رجوع","no_save_no","text_send","url_send","no_save","boten_add_1","no_boten1","no_boten_save","photo_no","no_photo_up","photo_up","photo_yas","photo_send_to","photo_send","save","boten_add","text_edd","setting_to","stop_fast","ren_fast","faste","sarch_id","delet_mtor","add_mtor","arad_admin","add_next_admin","add_admin","No_add_admin","wolcam","reply","chanl","user_all","trhep","delt_trhep","setting","no_send","yas_send","no_dlete","delte","rep_end","fos","ter","rep_ed","rep_dl","add_mshrf"])
def callback(call):
    global fast_run
    user = call.from_user
    chat_id = user.id
    first_name = user.first_name if user.first_name else "بدون اسم اول"
    last_name = user.last_name if user.last_name else "بدون اسم ثاني"
    full_name = f"{first_name} {last_name}" if last_name else first_name
    username = user.username if user.username else "بدون يوزر"
    language = user.language_code

    if call.data == 'add_admin':
        try:
            joining_data = rest(int(user_chat_admin[0]))
            db.reference(f'/Aministrtor/{int(user_chat_admin[0])}').set({
                    'full_name': full_name,
                    'username': username,
                    'language': language,
                    "joining": joining_data,
                    'created_at': created_at
                })
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
            bot.delete_message(chat_id,call.message.message_id)
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id , text="تم اضافة الادمن بنجاح ✅")
        try:
            bot.delete_message(chat_id,message_id=user_chat_admin[1])
            bot.send_message(user_chat_admin[0],"لقد تم ترقيتك الي ادمن في البوت 🤍\n الرجاء ارسال /start  \n لي ارسل لك لوحة الادمن 👨‍💻")
            bot.send_message(chat_id,"تمت ترقية الأدمن وتم إعلامه بذلك.✅")
            bot.answer_callback_query(call.id, f"تم إعلام {first_name} بترقيته مسؤولًا في البوت.")
        except:
            pass
        user_chat_admin.clear()
    elif call.data == "add_next_admin":
        bot.send_chat_action(chat_id, "typing")
        messagee = (
        "مرحباً يا أدمن\n"
        "لإضافة أدمن، الرجاء التأكد من أن الأدمن من ضمن مستخدمي البوت.\n"
        "يمكنك إرسال رابط المستخدم أو ID المستخدم أو @يوزر المستخدم."
        )

        mgs = bot.send_message(chat_id,messagee)
        bot.register_next_step_handler(mgs,admin_chat.admin_add)



    elif call.data == "arad_admin":
        ref = db.reference(f'/Aministrtor')
        data = ref.get()
        cont = 0
        text =''
        mass_text = ''
        if data is None:
            bot.send_message(chat_id,"نعتذر، حصل خطاء في قاعدة البيانات لا يوجد ادمن في قاعدة البيانات الرجاء التوصل مع المطور لحل هذه المشكلة.")
            return
        else:
            try:
                for user_ids in data:
                    ref = db.reference(f'/Aministrtor/{user_ids}')
                    data_us = ref.get()
                    cont+=1

                    for key, value in data_us.items():
                        chat = bot.get_chat(int(user_ids))

                        if cont == 1:
                            if key == "joining":
                                text = f"""╔════ ⸨ ID المستخدم: {user_ids}⸩ ════╗

الاسم : {chat.first_name if chat.first_name else "بدون اسم"} {chat.last_name if chat.last_name else ""}
يوزره : @{chat.username if chat.username else "بدون يوزر"}
تاريخ انشاء حسابه : {value}
وظايفته : مطور البوت 👑⚒️
"""
                            mass_text = text
                        else:
                            if key == "joining":
                                text = f"""║═════ ⸨ ID المستخدم: {user_ids}⸩ ═════║
اسمه : {chat.first_name if chat.first_name else "بدون اسم"} {" " + chat.last_name if chat.last_name else ""}
يوزره : @{chat.username if chat.username else "بدون يوزر"}
تاريخ انشاء حسابه : {value}
وظيفته : ادمن 🧑‍💻
"""


                            mass_text = f"{mass_text}\n{text}"
                mass_text = mass_text+"\n"+ "╝═════════ ⸨* انتهى. *⸩ ═════════╚"
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text= f"*{mass_text}*", parse_mode='Markdown')
            except Exception as e:
                print(e)
    elif call.data == 'No_add_admin':
        try:
            bot.delete_message(chat_id=chat_id, message_id=user_chat_admin[1])
            bot.send_message(chat_id,"تم الغاء اضافة الادمن ✅")
            user_chat_admin.clear()
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
            bot.delete_message(chat_id,call.message.message_id)
    elif call.data == "wolcam":
        try:
            keyboard = telebot.types.InlineKeyboardMarkup()
            btn1 = telebot.types.InlineKeyboardButton(text='اضافة رسالة الترحيب', callback_data='trhep')
            btn2 = telebot.types.InlineKeyboardButton(text='حذف رسالة الترحيب', callback_data='delt_trhep')
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "اختر احد الخيارات الاتيه : ",reply_markup=keyboard)

        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
            bot.delete_message(chat_id,call.message.message_id)
    elif call.data == "reply":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("حذف 🗑", callback_data="rep_dl")
        button3 = types.InlineKeyboardButton("اضافة 📥", callback_data="rep_end")
        markup.add(button1)
        markup.add(button3)
        #markup.add(button4)

        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text= "اختر أيًا من الخيارات التالية ✅", reply_markup=markup)
    elif call.data == "chanl":
        mse = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="*يرجى رفع البوت كأدمن في القناة أو المجموعة، ثم إرسال اسم المستخدم الخاص بالقناة أو تحويل رسالة من القناة.*", parse_mode='Markdown')


        bot.register_next_step_handler(mse, lambda message: handle_forward_or_text_message(message, chat_id))

    elif call.data == "user_all":
        mss = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = """*الرجاء إرسال رسالة ليتم ارسلها لي جميع المستخدمين : *\n\t       * انماط الخط*
[[+]] *خط عريض* : (`*text*`)
[[+]] `نص قابل للنسخ`: (*`text`*)
[[+]] _نص مائل_ : (`_text_`)
[[+]] ``نص صغير`` : (*``text``*)
[[+]] ***نص غامق ومائل ***: (`*** text ***` )
[[+]] [نص رابط](https://t.me/br1mg): (`[text](url)`)
```نص``` : (*```text```*)
                                    """,parse_mode='Markdown')
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='نعم', callback_data='yas_send')
        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_send')
        keyboard.add(btn1, btn2)
        bot.register_next_step_handler(mss, lambda messaga:((sand_all.append(messaga.text)),bot.edit_message_text(chat_id=chat_id, message_id=mss.message_id,text = f"*هل موفق هل ارسل هذا النص الي جميع المستخدمين؟* \nالنص:\n{messaga.text}",parse_mode='Markdown',reply_markup=keyboard),
        bot.delete_message(messaga.chat.id,messaga.message_id)))
    elif call.data == "setting":
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
               print("ERORROORRO")
    elif call.data == "delt_trhep":
        try:
            ref = db.reference(f'/Welcome Message/')
            data = ref.get()
            if data is None:
                bot.send_message(chat_id,"نعتذر، لا توجد رسالة ترحيب متاحة في الوقت الحالي.⛔️")
                return
            keyboard = telebot.types.InlineKeyboardMarkup()
            btn1 = telebot.types.InlineKeyboardButton(text='موفق 🗑', callback_data='delte')
            btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_dlete')
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "هل انت موفق على حذف رسالة الترحيب؟",reply_markup=keyboard)
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
            bot.delete_message(chat_id,call.message.message_id)
    elif call.data == "trhep":
        try:
            text = """*مرحبًا يا أدمن 🧑‍💻\nيرجى إرسال رسالة الترحيب ليتم إضافتها 📩\nمعلومات يمكن الاستفادة منها:*
[[+]] *إضافة الاسم الأول:* `{first_name}`
[[+]] *إضافة الاسم الثاني:* `{last_name}`
[[+]] *إضافة الاسم الكامل:* `{full_name}`
[[+]] *إضافة يوزر الشخص:* `{username}`
[[+]] *إضافة ID الشخص:* `{chat_id}`
[[+]] *إضافة لغة الشخص:* `{language}`
[[+]] *إضافة اسم المطور الأول:* \n`{admin_first_name}`
[[+]] *إضافة اسم المطور الثاني:* \n `{admin_last_name}`
[[+]] *إضافة اسم مطور البوت الكامل:*\n `{full_name_admin}`
[[+]] *إضافة يوزر المطور:* `{admin_user}`
[[+]] *إضافة اسم البوت الأول:* \n `{bot_first_name}`
[[+]] *إضافة اسم البوت الثاني:* \n `{bot_last_name}`
[[+]] *إضافة اسم البوت الكامل:* \n `{bot_full_name}`
[[+]] *إضافة يوزر البوت:* `{bot_username}`
\t       * انماط الخط*
[[+]] *خط عريض* : (`*text*`)
[[+]] `نص قابل للنسخ`: (*`text`*)
[[+]] _نص مائل_ : (`_text_`)
[[+]] ``نص صغير`` : (*``text``*)
[[+]] ***نص غامق ومائل ***: (`*** text ***` )
[[+]] [نص رابط](https://t.me/br1mg): (`[text](url)`)
```نص``` : (*```text```*)
            """
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = text,parse_mode='Markdown')
            bot.register_next_step_handler_by_chat_id(chat_id,text_start)
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
    elif call.data == "delt_trhep":
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "*تم الغاء العملية بنجاح ✅*",parse_mode='Markdown')
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
    elif call.data == "delte":
       try:
        ref = db.reference(f'/Welcome Message/')
        start_text.clear()
        ref.delete()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "*تم حذف رسالة الترحيب بنجاح ✅*",parse_mode='Markdown')
       except:
           bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)

    elif call.data == "no_dlete":
        sand_all.clear()
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "*تم الغاء عملية الحذف ✅*",parse_mode='Markdown')
        except:
            bot.answer_callback_query(call.id, "عذراً، انتهت صلاحية هذه الرسالة.⛔️", show_alert=True)
    elif call.data == "yas_send":
        user_id = call.from_user.id
        chat_id = user_id
        n = 0
        bind = 0
        ref = db.reference(f'/users/')
        data = ref.get()

        if not data:
            bot.send_message(chat_id, "لا يوجد مستخدمين لإرسال الرسالة لهم", parse_mode='Markdown')
            return

        for snede in data:

            try:

                chatt = bot.get_chat(snede)

                text = (f"""تم إرسال الرسالة الي:\n{chatt.first_name or ''} {chatt.last_name or ''}\nيوزره: @{chatt.username or 'غير متاح'}\nID المستخدم: {snede}""")


                textx, photos = information(snede)

                if sand_all:
                    n += 1
                    # إذا لم تكن هناك صورة، أرسل رسالة نصية
                    if not photos:
                        bot.send_message(chat_id, text)
                        bot.send_message(snede, f'*{sand_all[0]}*', parse_mode='Markdown')
                    else:
                        # إرسال الصورة مع الن
                        bot.send_photo(chat_id, photos, caption=text)
                        bot.send_message(snede, f'*{sand_all[0]}*', parse_mode='Markdown')

            except ApiTelegramException as e:

                if "Forbidden" in str(e):
                    bind += 1
                    bot.send_message(chat_id,f"فشل في إرسال الرسالة إلى {snede}: {e}")
                    user_ref = db.reference(f'users/{snede}')
                    user_ref.delete()


            bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text=f"*تم إرسال الرسالة إلى : {n} من الأشخاص 📩 \nفشل إرسال هذه الرسالة إلى : {bind} من الأشخاص 📩*",parse_mode='Markdown')

    elif call.data == "yas_send_admin":
        user_id = call.from_user.id
        chat_id = user_id
        n = 0
        bind = 0
        ref = db.reference(f'/Aministrtor/')
        data = ref.get()

        if not data:
            bot.send_message(chat_id, "لا يوجد ادمن لإرسال الرسالة لهم", parse_mode='Markdown')
            return

        for snede in data:

            try:

                chatt = bot.get_chat(snede)

                text = (f"""تم إرسال الرسالة الي:\n{chatt.first_name or ''} {chatt.last_name or ''}\nيوزره: @{chatt.username or 'غير متاح'}\nID المستخدم: {snede}""")


                textx, photos = information(snede)

                if sand_all:
                    n += 1
                    # إذا لم تكن هناك صورة، أرسل رسالة نصية
                    if not photos:
                        bot.send_message(chat_id, text)
                        bot.send_message(snede, f'*{sand_all[0]}*', parse_mode='Markdown')
                    else:
                        # إرسال الصورة مع الن
                        bot.send_photo(chat_id, photos, caption=text)
                        bot.send_message(snede, f'*{sand_all[0]}*', parse_mode='Markdown')

            except ApiTelegramException as e:

                if "Forbidden" in str(e):
                    bind += 1
                    bot.send_message(chat_id,f"فشل في إرسال الرسالة إلى {snede}: {e}")
                    user_ref = db.reference(f'users/{snede}')
                    user_ref.delete()
            bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text=f"*تم إرسال الرسالة إلى : {n} من الأشخاص 📩 \nفشل إرسال هذه الرسالة إلى : {bind} من الأشخاص 📩*",parse_mode='Markdown')

    elif call.data == "no_send":
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم الغاء العملية بنجاح✅")
        except:
            pass
    elif call.data == "no_send_admin":
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم الغاء العملية بنجاح✅")
        except:
            pass
    elif call.data == "rep_end":
        try:
            mas = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="الرجاء ادخال الرسالة الاساسية لي يتم الرد عليها :")
            bot.register_next_step_handler(mas,massege_Ass)
        except:
            pass
    elif call.data == "fos":
        try:
            bot.delete_message(chat_id,reply_ms[3])
            reply_ms.clear()
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم الغاء العملية بنجاح✅")
        except:
            pass
    elif call.data == "ter":
        db.reference(f'/reply/{reply_ms[2]}').set({
                 reply_ms[0] : reply_ms[1],
                'created_at': created_at
                })
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم اضافة الرسالة الرد بنجاح ✅")

    elif call.data == "rep_ed":
        ref = db.reference(f'/reply/')
        data = ref.get()
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="لا يوجد شىء لحذفه ⛔️")
        try:
            ref = db.reference(f'/reply/')
            data = ref.get()
            con = 0
            masse_text = '' ; text = ''
            if data is None:
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="لا يوجد شىء لعرضه ⛔️")
                return
            for red in data:
                ref = db.reference(f'/reply/{red}')
                data = ref.get()
                for key , value in data.items():

                    if  not key == "created_at":
                        con+=1
                        text = f"""╗═════ ⸨ *كود الرسالة *: `{red}`⸩ ═════╔
    📥 *الرسالة *:
    {key}
    📤 *رد الرسالة *:
    {value}\n
"""
                        if con == 1:
                            masse_text = text
                        else:
                            text = f"""║═════ ⸨ *كود الرسالة *: `{red}`⸩ ═════║
    📥 *الرسالة *:
        {key}
    📤 *رد الرسالة *:
        {value}\n
"""
                            masse_text = masse_text + text
            masse_text=masse_text+"╝═════════ ⸨* انتهى. *⸩ ═════════╚"
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*{masse_text}*",parse_mode='Markdown')
        except:
            pass
    elif call.data == "rep_dl":
        try:
            keyboard = InlineKeyboardMarkup()
            ref = db.reference(f'/reply/')
            data = ref.get()
            if data is None:
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*عذرا، لا يوجد رسالة لي حذفها ✅*",parse_mode='Markdown')
                return
            for da in data:
                ref = db.reference(f'/reply/{da}')
                data_da = ref.get()
                for key in data_da:
                    if key == "created_at":
                        continue
                    elif key == "caption":
                        continue
                    keyboard.add(InlineKeyboardButton(f"{key}🗑",callback_data=f"ragea_{key}"))
            keyboard.add(InlineKeyboardButton(f"رجوع الي القائمة",callback_data=f"رجوع"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر الرسالة لي يتم حذفها ✅*",parse_mode='Markdown',reply_markup=keyboard)

        except:
             bot.send_message(chat_id,"حدث خطاء اثناء ارسال الرسالة الي قاعدة البيانات")
    elif call.data == "add_mtor":
        ref = db.reference(f'/Aministrtor/')
        data = ref.get()
        markup = InlineKeyboardMarkup()
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="لا يوجد شىء لعرضه ⛔️")
            return
        for users in data:
            ref = db.reference(f'/Aministrtor/{users}')
            data_usu = ref.get()
            for key , value in data_usu.items():
                if key == "full_name":
                    markup.add(InlineKeyboardButton(f"{value}", callback_data=f"name_{users}"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "اختر شخص لي ترقيته الي ادمن",reply_markup=markup)

    elif call.data == "delet_mtor":
        ref = db.reference(f'/Bot_developer/')
        data = ref.get()
        markup = InlineKeyboardMarkup()
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="لا يوجد شىء لعرضه ⛔️")
            return
        for users in data:
            ref = db.reference(f'/Bot_developer/{users}')
            data_usu = ref.get()
            for key , value in data_usu.items():
                if key == "full_name":
                    markup.add(InlineKeyboardButton(f"{value}", callback_data=f"dlname_{users}"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "اختر شخص لي ترقيته الي ادمن",reply_markup=markup)
    elif call.data == "sarch_id":
        mse = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء إرسال id الشخص أو معرف الشخص مع تضمين العلامة @")
        bot.register_next_step_handler(mse,user_sarch)
    elif call.data == "faste":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(f"تشغيل الوضع ⚡️", callback_data=f"ren_fast"))
        markup.add(InlineKeyboardButton(f"ايقاف الوضع ⚡️", callback_data=f"stop_fast"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "اختر من الاوضع الاتيه.",reply_markup= markup)
    elif call.data == "ren_fast":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم تشغيل الوضع ⚡️")
        if not fast_run:
            fast_run = True

    elif call.data == "stop_fast":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم ايقاف الوضع ⚡️")
        if fast_run:
            fast_run = False
    elif call.data == "calculate_expression":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*🧮 اكتب مسألتك الرياضية لأحاول حلها:*",parse_mode='Markdown')
    # تسجيل الخطوة التالية لانتظار إدخال المستخدم
        bot.register_next_step_handler(call.message, solve_expression)

    elif call.data == "create_qr":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*📝 ادخل نص لوضعه في رمز QR:*",parse_mode='Markdown')
    # تسجيل الخطوة التالية لانتظار إدخال المستخدم
        bot.register_next_step_handler(call.message, generate_qr)
    elif call.data == "fetch_html":
        # تحديث حالة الجلسة إلى 'fetch_html'
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*يرجي العلم ان مش كل الصفح بيتم سحبها بسبب عدم قدره البوت في جلب المحتوا\n 📝 أدخل رابط الصفحة لسحب هيكل الـ HTML:*",parse_mode='Markdown')
        bot.register_next_step_handler(call.message, fetch_html)
    elif call.data == "create_files":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*من هنا يمكنك صنع ملفات.\nاختر صيغة الملفات من الأسفل:*",parse_mode='Markdown', reply_markup=file_format_markup())
    elif call.data == "carha":
        markup = types.InlineKeyboardMarkup()

        file_button = types.InlineKeyboardButton("صنع ملفات", callback_data='create_files')
        html_button = types.InlineKeyboardButton("سحب قوالب HTML", callback_data='fetch_html')
        calc_button = types.InlineKeyboardButton("حساب العمليات الرياضية", callback_data='calculate_expression')
        qr_button = types.InlineKeyboardButton("صنع QR", callback_data='create_qr')  # زر صنع QR

        markup.add(file_button)
        markup.add( html_button)
        markup.add(calc_button)  # إضافة زر حساب العمليات الرياضية
        markup.add(qr_button)  # إضافة زر صنع QR
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*👋 أهلاً بك!\nهذا مكان مخصص لأشياء عشوائية قد تفيدك.\nاستخدم الأزرار بالأسفل للتفاعل 👇\n*",parse_mode='Markdown', reply_markup=markup)
    elif call.data =="creas":
        ms = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*الرجاء اضافة اسم صيغة الملف :*",parse_mode='Markdown')
        bot.register_next_step_handler(ms, fldar)
    elif call.data == "setting_to":
        keyboard = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton(text="إرسال مشكلة للمطور", callback_data='report_issue')
        btn2 = InlineKeyboardButton("سرعة البوت ✨⚡️", callback_data='check_speed')
        btn3 = InlineKeyboardButton(text='اذاعة ادمن 📢', callback_data='admin_send_all')
        btn4 = InlineKeyboardButton(text="سحب ملف قاعدة البيانات من الاستضافة", callback_data='sql_shb')
        btn5 = InlineKeyboardButton(text='اشياء عشوائية', callback_data='carha')
        btn6 = InlineKeyboardButton(text='البحث عن شخص عن طريق Id', callback_data='sarch_id')
        btn7 = InlineKeyboardButton(text='الإدخال السريع ⚡️', callback_data='faste')
        btn8 = InlineKeyboardButton(text='الرجوع', callback_data='redback1')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(InlineKeyboardButton("اقتراح تعديل", callback_data='suggest_modification'))
        keyboard.add(btn6)
        keyboard.add(btn7)
        keyboard.add(InlineKeyboardButton("إنشاء كود جديد",callback_data="create_new_code"))
        keyboard.add(InlineKeyboardButton("جميع الاكواد",callback_data="code_all"))
        keyboard.add(btn8)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر احد الخيارات الاتيه : *",parse_mode='Markdown',reply_markup=keyboard)
    elif call.data == "redback1":
        if markup_key:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر احد الخيارات الاتيه : *",parse_mode='Markdown',reply_markup=markup_key[0])
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*عذرا، انتهت صلاحية هذا الزر :*",parse_mode='Markdown')
    elif call.data == "suggest_modification":
        bot.send_message(call.message.chat.id, "💡 اكتب اقتراحك الآن، أو أرسل صورة أو ملف وسأرسله للمطور.")
        bot.register_next_step_handler(call.message, handle_suggestion)
    elif call.data == "check_speed":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "⏳ انتظر، يتم قياس سرعة البوت...")
        start_time = time.time()
        m = bot.send_message(call.message.chat.id, "جاري قياس السرعة...")
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
        bot.edit_message_text(chat_id=chat_id, message_id = m.message_id, text = speed_feedback)

    elif call.data == "report_issue":
        bot.send_message(call.message.chat.id, "🛠️ ارسل مشكلتك الآن، وسيحلها المطور في أقرب وقت.")
        bot.register_next_step_handler(call.message, handle_report)
    elif call.data == "text_edd":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء إدخال الرد ليتم إضافته:")
        bot.register_next_step_handler(mes1, massege_red)

    elif call.data == "boten_add":
        if not chat_ida:
            mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء اضافة اسم للزر :")
            bot.register_next_step_handler(mes1, boten_red)
        elif chat_ida:
            mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء اضافة اسم للزر التالي :")
            bot.register_next_step_handler(mes1, boten_red)
    elif call.data == "photo_send":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء ارسال صورة ليتم رفعها :")
        bot.register_next_step_handler(mes1, photo_send)
    elif call.data == "save":
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='اضافة زر', callback_data='boten_add')
        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_boten_save')
        keyboard.add(btn1, btn2)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم الحفظ ✅\n هل تريد اضافة زر اخر؟",reply_markup=keyboard)
        print(reply_ms)
        print(Button)
        if reply_ms:
            message_ass.append(reply_ms[0])
        boten_neame.append(Button[0])
        reply_ms.clear()
        Button.clear()
    elif call.data == "photo_send_to":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء ارسال صورة ليتم حفظها :")
        bot.register_next_step_handler(mes1, photo_send_to)
    elif call.data == "photo_yas":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء ارسال وصف للصورة :")
        bot.register_next_step_handler(mes1, photo_yas)
    elif call.data == "photo_up":
        db.reference(f'/reply/{reply_ms[1]}').set({
                reply_ms[0] : reply_ms[2],
                "caption": reply_ms[3],
                'created_at': created_at
                })
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم رفع الصورة بنجاح ✅")
    elif call.data == "photo_no":
        db.reference(f'/reply/{reply_ms[1]}').set({
                reply_ms[0] : reply_ms[2],
                'created_at': created_at
                })
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم رفع الصورة بنجاح ✅")
    elif call.data == "no_boten_save":
        for x in range(len(text_boten)):
            boten_neame_text.update({boten_neame[x]:text_boten[x]})
        db.reference(f'/reply/{rednmper[0]}').set({
            message_ass[0]: {message_ass1[0]:boten_neame_text},
            'created_at': created_at
            })
        message_ass.clear()
        boten_neame_text.clear()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم عملية رفع الزر بنجاح ✅")
    elif call.data == "no_boten1":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء اضافة الرسالة التي تظهر فوق الازرار :")
        bot.register_next_step_handler(mes1, message_ass_as)
    elif call.data == "boten_add_1":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء اضافة الرسالة التي تظهر فوق الازرار :")
        bot.register_next_step_handler(mes1, message_ass_as)
    elif call.data == "no_save":
        delete_image(مسار_الصورة[0])
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم الغاء العملية بنجاح ✅")
    elif call.data == "url_send":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "ارسل الربط ليتم وضعه في الزر :")
        bot.register_next_step_handler(mes1, photo_send)
    elif call.data == "no_save_no":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "ارسل الربط ليتم وضعه في الزر :")
        text_boten.clear()
        reply_ms.clear()
        message_ass.clear()
    elif call.data == "text_send":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "ارسل النص ليتم وضعه في الزر :")
        bot.register_next_step_handler(mes1, photo_send)
    elif call.data == "رجوع":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("حذف 🗑", callback_data="rep_dl")
        button3 = types.InlineKeyboardButton("اضافة 📥", callback_data="rep_end")
        markup.add(button1)
        markup.add(button3)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر أيًا من الخيارات التالية ✅*",parse_mode='Markdown',reply_markup= markup)
    elif call.data == "usere_adda":
        ref = db.reference(f'/users/')
        data = ref.get()
        try:
            total_users = len(data)
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*(———————————)\n\nاحصائيات البوت :\nعدد المستخدمين : {total_users}\n\n(———————————)*",parse_mode='Markdown')
        except Exception as e:
            logging.error(f"Error in show_statistics: {e}")
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*⚠️ حدث خطأ أثناء عرض الإحصائيات.*",parse_mode='Markdown')
    elif call.data == "admin_send_all":
        mss = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = """*الرجاء إرسال رسالة ليتم ارسلها لي جميع الادمن : *\n\t       * انماط الخط*
[[+]] *خط عريض* : (`*text*`)
[[+]] `نص قابل للنسخ`: (*`text`*)
[[+]] _نص مائل_ : (`_text_`)
[[+]] ``نص صغير`` : (*``text``*)
[[+]] ***نص غامق ومائل ***: (`*** text ***` )
[[+]] [نص رابط](https://t.me/br1mg): (`[text](url)`)
```نص``` : (*```text```*)
                                    """,parse_mode='Markdown')
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='نعم', callback_data='yas_send_admin')
        btn2 = telebot.types.InlineKeyboardButton(text='لا', callback_data='no_send_admin')
        keyboard.add(btn1, btn2)
        bot.register_next_step_handler(mss, lambda messaga:((sand_all.append(messaga.text)),bot.edit_message_text(chat_id=chat_id, message_id=mss.message_id,text = f"*هل موفق هل ارسل هذا النص الي جميع المستخدمين؟* \nالنص:\n{messaga.text}",parse_mode='Markdown',reply_markup=keyboard),
        bot.delete_message(messaga.chat.id,messaga.message_id)))
    elif call.data == "add_mshrf":
        mss = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text ="*الرجاء إرسال اسم المستخدم (يبدأ بـ @) أو إرسال معرف المستخدم(ID).*",parse_mode='Markdown')
        bot.register_next_step_handler(mss, add_moshraf)
@bot.callback_query_handler(func= lambda call:(call.data.startswith("college_") or call.data.startswith("subject_") or call.data.startswith("grou_")) or call.data in(["rjog_sec","add_cout","non_cout","Not_group","sec_yas","sec_no","create_new_code","code_all"]))
def call_back(call):
    global cout,Enter_add_info
    chat_id = call.message.chat.id
    if call.data.startswith("college_"):
        sec = call.data.split("_")[1]
        if sec not in Group_idE:
            Group_idE.append(sec)#2
        fja.append(sec)
        keyboard = InlineKeyboardMarkup()
        for key, valuo in college_departments.items():
            if sec == key:
                for keya,valu in valuo.items():
                    if keya == fousol.get(cout):
                        for keyx,aa in dict(valu).items():
                            for xs, a in dict(valu).items():
                                keyboard.add(InlineKeyboardButton(text=f'{a}', callback_data=f'subject_{keyx}'))
                            break
                if cout == 1:
                    keyboard.add(InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
                elif cout >1:
                    keyboard.add(InlineKeyboardButton("⬅",callback_data="non_cout"),InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
                bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text =f"*الان، اختر المقرار الخاص بمجموعك من السيم : {keya}*",parse_mode='Markdown',reply_markup= keyboard)
    elif call.data == "rjog_sec":
        keyboard = InlineKeyboardMarkup()
        for x in college_departments:
            btn1 = InlineKeyboardButton(text=f'{x}', callback_data=f'college_{x}')
            keyboard.add(btn1)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text ="*اختر احد الاقسام :*",parse_mode='Markdown',reply_markup= keyboard)
    elif call.data == "add_cout":
        cout+=1
        keyboard = InlineKeyboardMarkup()
        for key, valuo in college_departments.items():
            if key in fja:
                for keya,valua in valuo.items():
                    if keya == fousol.get(cout):

                        for keyx in valua:

                            for xs, a in dict(valua).items():
                                keyboard.add(InlineKeyboardButton(text=f'{a}', callback_data=f'subject_{xs}'))
                            break
                if cout == 1:
                    keyboard.add(InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
                elif cout >1:
                    keyboard.add(InlineKeyboardButton("⬅",callback_data="non_cout"),InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
                bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text =f"*الان، اختر المقرار الخاص بمجموعك من السيم : {keya}*",parse_mode='Markdown',reply_markup= keyboard)
    elif call.data == "non_cout":
        cout-=1
        keyboard = InlineKeyboardMarkup()
        for keya,valua in valuo.items():
            if keya == fousol.get(cout):
                for keyx in valua:
                    for xs, a in dict(valua).items():
                        keyboard.add(InlineKeyboardButton(text=f'{a}', callback_data=f'subject_{xs}'))
                    break
        if cout == 1:
            keyboard.add(InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
        elif cout >1:
            keyboard.add(InlineKeyboardButton("⬅",callback_data="non_cout"),InlineKeyboardButton(text='الرجوع الي القائمة', callback_data='rjog_sec'),InlineKeyboardButton("➡",callback_data="add_cout"))
        bot.edit_message_text(chat_id=chat_id,text =f"*الان، اختر المقرار الخاص بمجموعك من السيم : {keya}*",parse_mode='Markdown',reply_markup= keyboard)

    elif call.data.startswith("subject_"):
            sub = call.data.split("_")[1]
            print(Group_idE)
            user = bot.get_chat(Group_idE[1])
            first_name = user.first_name if user.first_name else "بدون اسم اول"
            last_name = user.last_name if user.last_name else "بدون اسم ثاني"
            full_name = f"{first_name} {last_name}" if last_name else first_name
            username = user.username if user.username else "بدون يوزر"
            Group = bot.get_chat(Group_idE[0])
            bot_user = bot.get_me()
            bot_member = bot.get_chat_member(Group_idE[0],bot_user.id)
            if bot_member.status in ['administrator','creator']:
                db.reference(f'/Supervisor/{Group_idE[0]}').set({
                "Name Group" : Group.title,
                "user_id" : Group_idE[1],
                "sec": Group_idE[2],
                "subject":sub,
                "Name": full_name,
                "username": f"@{username}",
                "username_Group": f"@{Group.username}"
                })
                Enter_add_info = False
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                markup.add(KeyboardButton("معلومات"))
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text ="*تم اضافة البيانات✅*",parse_mode='Markdown')
                bot.send_message(chat_id,"الان يمكنك ادارات المجموعة عن طريق البوت✅",reply_markup=markup)

                ref = db.reference(f'/SuperTS/{chat_id}')
                ref.delete()
                Group_idE.clear()
                GRoup.clear()
        
            # bot.delete_message(chat_id,call.message.message_id)
    elif call.data == "create_new_code":
        if (call.message.chat.id) == admin[0]:
            code = generate_random_code()  # توليد كود عشوائي
            db.reference(f'/codes/{code}').set({
                'created_by': admin[0],
                'used_by': None,
                'created_at': created_at
                })
            bot.answer_callback_query(call.id, f"تم إنشاء الكود: {code}")
            bot.send_message(call.message.chat.id, f"تم إنشاء الكود: `{code}`",parse_mode='Markdown')
        else:
            bot.answer_callback_query(call.id, "ليس لديك صلاحية للقيام بهذا الإجراء.")
    elif call.data == "code_all":
        scode1 = ''
        if (call.message.from_user.id) == admin[0]:
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
                bot.send_message(admin[0],scode1,parse_mode='Markdown')
            except Exception as e:
                bot.send_message(admin[0], "لا يوجد اكواد :")
bot.polling()