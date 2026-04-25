from info_bot import *
from main_def import *
xc = True
admin_chat = Admin(bot, admin)
user_chat = User(bot, user_list)

@bot.message_handler(commands=['start',"id","help"])
def message_wolacm(message):
    user = message.from_user
    chat_id = user.id
    if is_bot_or_fake(message.from_user):
        bot.send_message(message.chat.id, "🚫 لا يمكنك التصويت، حسابك غير مؤهل.")
        banned_users.add(chat_id)
        return
    if not check_subscription(chat_id):
        send_subscription_message(chat_id)
        return
    first_name = user.first_name if user.first_name else "بدون اسم اول"
    last_name = user.last_name if user.last_name else "بدون اسم ثاني"
    full_name = f"{first_name} {last_name}" if last_name else first_name
    username = user.username if user.username else "بدون يوزر"
    language = user.language_code
    is_Bot = user.is_bot   
    try:
        is_admin = admin_chat.admin_start(chat_id)
        tset = SARCH_USER(chat_id)
        ref = db.reference(f'/users/{chat_id}')
        data = ref.get()
        if data is None:
            joining_data = rest(chat_id)
            db.reference(f'/users/{chat_id}').set({
                    'full_name': full_name,
                    'username': username,
                    'language': language,
                    "joining": joining_data,
                    "is_Bot": is_Bot,
                    
                    'created_at': created_at
                })
        else:
            if message.text.startswith('/start'):
                if is_admin:
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
                    if candidates:
                        markup.add(KeyboardButton(boten_key_name.get("stop_key")))
                    else:    
                        markup.add(button7)
                    if xc == True:
                        for name_boten in KeyButton:
                            markup.add(KeyboardButton(f'{name_boten}'))
                    if not candidates:  
                        bot.reply_to(message,f"مرحبا بك يا ادمن  \n {full_name} 🤍\n في لوحة تحكم الادمن اختر احد الخيارات ليتم تنفيذها",reply_markup=markup)
                        return
                    if candidates is not None:
                        send_candidates_list(chat_id)        
                    # bot.answer_callback_query(message.chat.id, "يرجى الانتظار قليلًا قبل التصويت مرة أخرى.", show_alert=True)
                else:
                    if fake_user(message.from_user):
                        captcha_text, img_path = generate_captcha()
                        user_captcha[message.chat.id] = captcha_text
                        # إرسال الصورة للمستخدم
                        with open(img_path, 'rb') as img:
                            bot.send_photo(message.chat.id, img, caption="يرجى إدخال النص  الموجود في الصورة التحقق:")
                            return
                    if not candidates:
                        ref = db.reference(f'/Welcome Message/')
                        data = ref.get()
                        if len(start_text)>=1:
                            text = edit_text_start(message,start_text[0],chat_id)
                            text = str(text)
                            bot.send_message(chat_id,f"{text}",parse_mode='Markdown')
                        else:
                            if data is not None:
                                for key,Value in data.items():
                                    if key == "Message":
                                        text = edit_text_start(message,Value,chat_id)
                                        text = str(text)
                                        bot.send_message(chat_id,f"{text}",parse_mode='Markdown')
                                        start_text.append(text)
                    if candidates is not None:
                        send_candidates_list(chat_id)
                            
                            
            elif message.text.startswith('/id'):
                bot.reply_to(message, f"*YOUR ID* : "f'`{chat_id}`', parse_mode='Markdown')        
            elif message.text.startswith('/help'):
                bot.reply_to(message,"اذا كان هناك خطاء الرجاء التوصل مع المطور \n @ko_2s")
    except Exception as e:
        print(e)
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    handle_all_messages1(message) or check_captcha(message)
#lock

@bot.message_handler(content_types=[photo,voice,audio,document,sticker,video,video_note,location,contact])
def lock (message):
    
    if message.content_type in op_close:
        
        if not op_close.get(message.content_type) == "None":

            bot.delete_message(message.chat.id, message.message_id)
@bot.callback_query_handler(func= lambda call: call.data in ["no_send_admin","yas_send_admin",'admin_send_all',"stetes","viewa_tsoey","man_hoa","usere_adda","redback1","suggest_modification","check_speed","creas","sql_shb","report_issue","send_private_message","calculate_expression","create_qr","fetch_html","create_files","carha","رجوع","no_save_no","text_send","url_send","no_save","boten_add_1","no_boten1","no_boten_save","photo_no","no_photo_up","photo_up","photo_yas","photo_send_to","photo_send","save","boten_add","text_edd","setting_to","stop_fast","ren_fast","faste","sarch_id","delet_mtor","add_mtor","arad_admin","add_next_admin","add_admin","No_add_admin","wolcam","reply","chanl","user_all","trhep","delt_trhep","setting","no_send","yas_send","no_dlete","delte","rep_end","fos","ter","rep_ed","rep_dl"])
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
            # bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id , text="تم اضافة الادمن بنجاح ✅")
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
    elif call.data  == "man_hoa":
        ntejt = {}
        m1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*جاري حساب فحص الاصوات لي اعلان النتيجه ⌛️*",parse_mode='Markdown')
        t1 = time.time()
        for ke, va in candidates1.items():
            name = va['name']      # اسم المتسابق
            vod = va['votes']      # عدد الأصوات
            sec = va['section']    # اسم المسابقة
            
            if sec not in ntejt:
                ntejt[sec] = []
            
            ntejt[sec].append({'name': name, 'votes': vod})
        for sec, participants in ntejt.items():
            # إيجاد أعلى عدد من الأصوات في المسابقة
            max_votes = max(participant['votes'] for participant in participants)
            
            # جمع المتسابقين الذين حصلوا على أعلى عدد من الأصوات
            winners = [participant['name'] for participant in participants if participant['votes'] == max_votes]
            
            # التحقق من وجود تعادل أو فائز واحد
            try:
                bot.delete_message(chat_id,m1.message_id) 
            except:
                pass      
            if len(winners) > 1:
                # حالة التعادل
                winners_text = ', '.join([f"{name} 🗳️ بعدد أصوات: {max_votes}" for name in winners])
                bot.send_message(chat_id,f"*🔔 النتيجة هي تعادل بين المتسابقين في {sec}:\n\n{winners_text}*",parse_mode='Markdown')
            else:
                # حالة فوز متسابق واحد
                bot.send_message(chat_id,f"*🎉 الفائز في {sec} هو: {winners[0]} 🏆 بعدد أصوات: {max_votes}*",parse_mode='Markdown')
        tss = time.time() - t1
        
        bot.send_message(chat_id,f"*الزمن المستغرق بالثواني: {tss:2f} ثانية*",parse_mode='Markdown')             
    elif call.data == "viewa_tsoey":
        ref = db.reference(f'/User_data/')
        data = ref.get()
        if not candidates:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*عذرًا، لم تقم ببدء المسابقة ✅*",parse_mode='Markdown')
            return
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*عذرا، لايوجد متسابقين ✅*",parse_mode='Markdown')
            return
        keyboard = InlineKeyboardMarkup()
        for sec in data:
            keyboard.add(InlineKeyboardButton(f"{sec}",callback_data=f"viewtso_{sec}"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر احد الخيارات الاتيه : *",parse_mode='Markdown',reply_markup=keyboard)  
    elif call.data == "stetes":
        #عدد المتسابقين
        #عدد الاقسام
        #نسبة المتسابقين الذين صوتو
        #الاشخاص الذين تم حظرهم
        ref = db.reference(f'/section/')
        data = ref.get()
        nmp_sec = len(data) if len(data) else 0
        nemp_user = 0
        ref = db.reference(f'/User_data/')
        data = ref.get()
        user_votes1 = user_votes2[0]
        if data is None:
            nemp_user = 0
        else:
            for x in data:
                ref = db.reference(f'/User_data/{x}')
                data1 = ref.get()
                nemp_user = len(data1) + nemp_user
        #نجيبو عدد مستخدمسن البوت
        #قاعد نكتب في الكود الساعة 4 خايف نلخبط لذلك قاعدت نكتب بي #🙂
        ref = db.reference(f'/users/')
        data = ref.get()
        مستخدمين_البوت = len(data) if len(data) else None
        النسبة_المئوية = f"{((len(user_votes1))/مستخدمين_البوت * 100)}%" if f"{((len(user_votes1))/مستخدمين_البوت * 100)}%" else "لا توجد بيانات بعد"
        ban = len(banned_users)

        text = f"""
📊 تقرير إحصائي 📊
-------------------------------
👥 عدد المتسابقين        : {nemp_user}
🏷️ عدد الأقسام           : {nmp_sec}
📈 نسبة التصويت         : {النسبة_المئوية}%
🚫 الأشخاص المحظورين  : {ban}
-------------------------------
"""
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*{text}*",parse_mode='Markdown')
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
@bot.callback_query_handler(func= lambda call: call.data in (["photo_op","voice_op","audio_op","document_op","sticker_op","video_op","video_note_op","location_op","contact_op","photo_close","voice_close","audio_close","document_close","sticker_close","video_close","video_note_close","location_close","contact_close"]))
def callbacd(call):
    global photo,voice,audio,document,sticker,video,video_note,location,contact,op_close,mtargam
    close.clear()
    main_callbacd(call)
@bot.callback_query_handler(func= lambda call:(call.data.startswith("sec_") or call.data.startswith("icon_") or call.data.startswith("delicon_") or call.data.startswith("dlesec_") or call.data.startswith("name_") or call.data.startswith("dlname_") or call.data.startswith("dletuser_") or call.data.startswith("vote_") or call.data.startswith("lockel_") or call.data.startswith("ragea_") or call.data.startswith("create_") or call.data.startswith("deletusrr_") or call.data.startswith("viewtso_") or call.data.startswith("go1_") or call.data.startswith("tims_")) or call.data in ["alkama1","alkama","dlet_sec","dlet_icon","add_icon","change_icon1","section","non_delet","no_totheg","totheg","tery","fosy","change_icon","add_candidate","add_section","add_tim","no_tim","tim_adde","tiemard","tameas"])
def call_backads(call):
    global vote_icon,lset,call_data
    user = call.from_user
    chat_id = user.id
    first_name = user.first_name if user.first_name else "بدون اسم اول"
    last_name = user.last_name if user.last_name else "بدون اسم ثاني"
    full_name = f"{first_name} {last_name}" if last_name else first_name
    username = user.username if user.username else "بدون يوزر"
    language = user.language_code
    if call.data.startswith("sec_"):
        sec_nmper.clear()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم اختر القسم واضافة المتسابق بنجاح ✅*",parse_mode='Markdown')
        sec_nem = call.data.split("_")[1]
        sec = str(sec_nem)
        ref = db.reference(f'/User_data/{sec}')
        data = ref.get()

        if data is None:
            data_send = f"اسم المتسابق : {user_list[0]}\n القسم : {sec}"
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='توثيق ✅', callback_data='totheg')
            btn2 = InlineKeyboardButton(text='لا', callback_data='no_totheg')
            keyboard.add(btn1, btn2)
            bot.send_message(chat_id,f"هل تريد توثيق هذه البيانات\n{data_send}",reply_markup= keyboard)
            
            name_user1.append(f"user : 1")
            sec_nmper.append(sec)
        else:
            for s in data:
                name= s
            name = int(name.split(":")[1])
            name+=1
            data_send = f"اسم المتسابق : {user_list[0]}\n القسم : {sec}"
            keyboard = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(text='توثيق ✅', callback_data='totheg')
            btn2 = InlineKeyboardButton(text='لا', callback_data='no_totheg')
            keyboard.add(btn1, btn2)
            sec_nmper.append(sec)
            name_user1.append(f"user : {name}")
            bot.send_message(chat_id,f"هل تريد توثيق هذه البيانات\n{data_send}",reply_markup= keyboard)
    elif call.data.startswith("icon_"):
        vote_icon.clear()
        
        try:
            vote_icon1 = call.data.split("_")[1]
            vote_icon.append(vote_icon1)
            bot.answer_callback_query(call.id, f"✅ تم تغيير الأيقونة إلى {vote_icon[0]}.")
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("➕ إضافة متسابق", callback_data="add_candidate"))
            markup.add(InlineKeyboardButton(f"🔄 تغيير أيقونة التصويت (حاليًا: {vote_icon[0]})", callback_data="change_icon1"))
            markup.add(InlineKeyboardButton("حذف قسم 🗑", callback_data="dlet_sec"))
            markup.add(InlineKeyboardButton("➕ إضافة قسم", callback_data="add_section"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "🔧 لوحة التحكم:",reply_markup=markup)
        
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء تغيير الأيقونة: {e}")
    elif call.data.startswith("delicon_"):
        try:
            vote_dlet = call.data.split("_")[1]
            emoji_list.remove(f"{vote_dlet}")
            if vote_icon[0] == vote_dlet:
                vote_icon.clear()
                vote_icon.append("🔥")
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("➕ إضافة متسابق", callback_data="add_candidate"))
            markup.add(InlineKeyboardButton(f"🔄 تغيير أيقونة التصويت (حاليًا: {vote_icon[0]})", callback_data="change_icon1"))
            markup.add(InlineKeyboardButton("حذف قسم 🗑", callback_data="dlet_sec"))
            markup.add(InlineKeyboardButton("➕ إضافة قسم", callback_data="add_section"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "🔧 لوحة التحكم:",reply_markup=markup)
        
        except ValueError:
            bot.answer_callback_query(call.id, f"عذرا، لا يمكنك حذف الايقوانة الافتراضيه ⛔️")
        except Exception as e:

            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء حذف الأيقونة: {e}")
        bot.answer_callback_query(call.id, f"✅ تم حذف الأيقونة {vote_dlet}.")
    elif call.data.startswith("dlesec_"):
        try:
            sec_nmper.clear()
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم حذف القسم بنجاح ✅*",parse_mode='Markdown')
            sec_nem = call.data.split("_")[1]
            sec_nem = int(sec_nem)
            sec = section[sec_nem]
            section.remove(sec)
        except Exception as e:
            bot.send_message(chat_id,f"حدث خطاء {e}")
    elif call.data.startswith("name_"):
        user_mtor = call.data.split("_")[1]
        user_mtor = int(user_mtor)
        chat_mtor = bot.get_chat(user_mtor)
        first_name = chat_mtor.first_name if chat_mtor.first_name else "بدون اسم اول"
        last_name = chat_mtor.last_name if chat_mtor.last_name else "بدون اسم ثاني"
        full_name = f"{first_name} {last_name}" if last_name else first_name
        username = chat_mtor.username if chat_mtor.username else "بدون يوزر"
        ref = db.reference(f'/Bot_developer/')
        data = ref.get()
        if data is None:
            db.reference(f'/Bot_developer/{user_mtor}').set({
                        "Name" : f"{full_name}",
                        "full_name": full_name,
                        "username" : username,
                        "add_you" : chat_id,
                        'created_at': created_at
                        })
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم ترقية الادمن الي مطور بنجاح ✅")
            bot.send_message(user_mtor,"مبروك لقد اصبحت مطور للبوت 🎉")
            return
        for usr in data:
            if int(usr) == user_mtor: 
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="هذا الادمن اصبح مطور بلفعل ✅")
                return
        db.reference(f'/Bot_developer/{user_mtor}').set({
                    "Name" : f"{full_name}",
                    "full_name": full_name,
                    "username" : username,
                    "add_you" : chat_id,
                    'created_at': created_at
                    })
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم ترقية الادمن الي مطور بنجاح ✅")
        bot.send_message(user_mtor,"مبروك لقد اصبحت مطور للبوت 🎉")
    elif call.data.startswith("dlname_"):
        user_mtor = call.data.split("_")[1]
        user_mtor = int(user_mtor)
        ref = db.reference(f'/Bot_developer/{user_mtor}')
        ref.delete()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم حذف المطور بنجاح ✅")
    elif call.data.startswith("dletuser_"):
        sec = call.data.split("_")[1]
        user_dleat = call.data.split("_")[2]
        ref = db.reference(f'/User_data/{sec}/{user_dleat}')
        ref.delete()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم حذف المتسابق بنجاح ✅")
    elif call.data.startswith("vote_"):
        user_id = call.from_user.id
        user_chat_id.append(user_id)
        candidate_key = call.data.split("_")[1]

        # تحقق إذا كان الحساب مزيفًا أو روبوتًا
        if is_bot_or_fake(call.from_user):
            bot.answer_callback_query(call.id, "🚫 لا يمكنك التصويت. حسابك محظور.", show_alert=True)
            banned_users.add(user_id)
            return

        # تحقق إذا كان المستخدم قد قام بالتصويت مسبقًا
        if user_id in user_votes:
            bot.answer_callback_query(call.id, "❗️ لقد قمت بالتصويت مسبقًا ولا يمكنك التصويت مرة أخرى.")
            return

        try:
            # تسجيل التصويت الجديد
            candidates[candidate_key]['votes'] += 1
            #هنا مكان تسجيل التصويت مره واحده
            user_votes[user_id] = candidate_key
            chat = bot.get_chat(user_id)
            first_name = chat.first_name if chat.first_name else "بدون اسم اول"
            last_name = chat.last_name if chat.last_name else "بدون اسم ثاني"
            full_name = f"{first_name} {last_name}" if last_name else first_name
            username = chat.username if chat.username else "بدون يوزر"
            section = candidates[candidate_key]['section']
            db.reference(f'/Votes/{section}/{candidate_key}/{user_id}').set({
                        "Name" : f"{full_name}",
                        "vote number" : f"{candidates[candidate_key]['votes']}",
                        "username" : username,
                        "chat_id" : user_id,
                        'created_at': created_at
                        })

            # تحديث رسالة التصويت بعد تسجيل الصوت
            update_vote_buttons(call.message.chat.id, call.message.message_id, candidate_key)

            bot.answer_callback_query(call.id, "✅ تم تسجيل تصويتك بنجاح!")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"❌ حدث خطأ أثناء التصويت: {e}")

    elif call.data.startswith("lockel_"):
        name = call.data.split("_")[1]
        dac = key_keu[0]
        dac = dict(dac)
        link = dac.get(name)
        text = dac.get(name)
        storage =  re.compile((r"https?://storage"))
        if storage.search(link):
            bot.delete_message(chat_id,key_keu[1])
            bot.send_photo(chat_id,link)
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = text )
         
    elif call.data.startswith("ragea_"):
        name = call.data.split("_")[1]
        storage =  re.compile((r"https?://storage"))
        ref = db.reference(f'/reply/')
        data = ref.get()
        for da in data:
            ref1 = db.reference(f'/reply/{da}')
            data = ref1.get()
            for key , valuo in dict(data).items():
                if key == "created_at":
                        continue
                elif key == "caption":
                        continue
                if key == name:
                    if valuo:
                        if isinstance(valuo, dict):
                            for keya , valuoa in valuo.items():
                                if isinstance(valuoa, dict):
                                    for keys , valuos in valuoa.items():
                                        if storage.search(valuos):
                                            photo = (str(valuos).split("/"))[-1]
                                            delete_image(photo)
                                            ref1.delete()
                                            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم حذف الرسالة بنجاح ✅🗑*",parse_mode='Markdown')
                        elif storage.search(valuo):
                            photo = (str(valuo).split("/"))[-1]
                            delete_image(photo)
                            ref1.delete()
                            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم حذف الرسالة بنجاح ✅🗑*",parse_mode='Markdown')
                        else:
                            ref1.delete()
                            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم حذف الرسالة بنجاح ✅🗑*",parse_mode='Markdown')                   
                    
    elif call.data.startswith("create_"):
        file_format = call.data.split('_')[1]

        bot.send_message(call.message.chat.id, f"📝 أدخل محتوى الملف بصيغة {file_format} لحفظه:")
        bot.register_next_step_handler(call.message, lambda msg: save_file(msg, file_format))
    elif call.data.startswith("deletusrr_"):
        sec = call.data.split('_')[1]
        ref = db.reference(f'/User_data/{sec}')
        data = ref.get()
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*لا يوجد متسابق في هذا القسم ❌*",parse_mode='Markdown')
            return
        else:
            markup = InlineKeyboardMarkup()
            for x in data:
                ref = db.reference(f'/User_data/{sec}/{x}')
                data_s = ref.get()
                for key , valuo in dict(data_s).items():
                    if key == "Name":
                        markup.add(InlineKeyboardButton(f"{valuo} 🗑",callback_data=f"dletuser_{sec}_{x}"))
            markup.add(InlineKeyboardButton(text = f"رجوع", callback_data=f"alkama1"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر متسابق لي حذفه :*",parse_mode='Markdown',reply_markup=markup)
    elif call.data.startswith("viewtso_"):
        sec = call.data.split('_')[1]
        ref = db.reference(f'/User_data/{sec}')
        data = ref.get()
        if data is None:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*لا يوجد متسابق في هذا القسم ❌*",parse_mode='Markdown')
            return
        else:
            markup = InlineKeyboardMarkup()
            for x in data:
                ref = db.reference(f'/User_data/{sec}/{x}')
                data_s = ref.get()
                for key , valuo in dict(data_s).items():
                    if key == "Name":
                        markup.add(InlineKeyboardButton(f"{valuo}",callback_data=f"go1_{valuo}"))
            markup.add(InlineKeyboardButton(text = f"رجوع", callback_data=f"viewa_tsoey"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر متسابق لي عرض عداد التصويت الخاص به :*",parse_mode='Markdown',reply_markup=markup)
    elif call.data.startswith("go1_"):
        name = call.data.split('_')[1]
        lis_vod = candidates.get(name)
        for key , valuo in dict(lis_vod).items():
            if key == "votes":
                if valuo == 0:
                    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*لم يتم التصويت لي {name} عداد اصواته صفر*",parse_mode='Markdown')
                    return
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*عدد اصوات {name} :{valuo}*",parse_mode='Markdown')
                return
    elif call.data.startswith("tims_"):
        try:
            tim = call.data.split('_')[1]
            if len(tim) > 1:
                duration_seconds = parse_duration(tim)
                if duration_seconds is None:
                    
                    bot.send_message(chat_id, "الرجاء إدخال المدة بصيغة صحيحة (ساعة:دقيقة).")
                    return
            else:
                # إذا لم يتم تحديد المدة، يتم تحديد مدة افتراضية (ساعة)
                duration_seconds = 60 * 60

            # بدء المسابقة
            start_competition(chat_id, duration_seconds,call)
    
        except Exception as e:
            bot.send_message(chat_id, f"حدث خطأ: {str(e)}")
    elif call.data == "alkama1":
        if markup_key1:
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر القسم الذي يوجد فيه المستخدم:*",parse_mode='Markdown',reply_markup= markup_key1[0])
        else:
            ref = db.reference(f'/User_data/')
            data = ref.get()
            markup = InlineKeyboardMarkup()
            if data is None:
                bot.send_message(chat_id=chat_id, text="لا يوجد شىء متسابقين ⛔️")
                return
            for sec in data:
                markup.add(InlineKeyboardButton(f"{sec}" , callback_data= f"deletusrr_{sec}"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*اختر القسم الذي يوجد فيه المستخدم:*",parse_mode='Markdown',reply_markup= markup)
            markup_key1.append(markup)
    elif call.data == "add_candidate":
        mse = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*🔤 أرسل اسم المتسابق:*",parse_mode='Markdown')
        bot.register_next_step_handler(mse, user_chat.add_user)
    elif call.data == "add_section":
        if chat_id in admin:
            try:
                mse = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*🔤 أرسل اسم القسم الجديد:*",parse_mode='Markdown')
                bot.register_next_step_handler(mse, add_section)
            except Exception as e:
                bot.send_message(call.message.chat.id, f"حدث خطأ أثناء إضافة القسم: {e}")
        else:
            bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات لإضافة قسم.")
    elif call.data == "tery":
        text = kasamem[0]
        kasamem.clear()
        section.append(text)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تمت عملية رفع القسم ✅*",parse_mode='Markdown')
        bot.answer_callback_query(call.id, "تم رفع القسم بنجاح ✅")
        db.reference(f'/section/{text}/').set({
                        "full_name": full_name,
                        "username" : username,
                        "chat_id" : chat_id,
                        'created_at': created_at
                        })
        if fast_run:
            mse = bot.send_message(chat_id,f"*🔤 أرسل اسم القسم الجديد التالي :*",parse_mode='Markdown')
            bot.register_next_step_handler(mse, add_section)
    elif call.data == "fosy":
        kasamem.clear()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم الغاء رفع القسم ✅*",parse_mode='Markdown')
        bot.answer_callback_query(call.id, "تم الغاء رفع القسم ✅")
    elif call.data == "totheg":
        db.reference(f'/User_data/{sec_nmper[0]}/{name_user1[0]}').set({
                        "Name" : f"{user_list[0]}",
                        "full_name": full_name,
                        "username" : username,
                        "chat_id" : chat_id,
                        'created_at': created_at
                        })
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم رفع المستخدم بنجاح ✅*",parse_mode='Markdown')    
        name_user1.clear()
        user_list1.clear()
        if fast_run:
            mse = bot.send_message(chat_id,text=f"*🔤 أرسل اسم المتسابق التالي :*",parse_mode='Markdown')
            bot.register_next_step_handler(mse, user_chat.add_user)
    elif call.data == "no_totheg":
        keyboard = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='تغير القسم', callback_data='section')
        btn2 = telebot.types.InlineKeyboardButton(text='اضافة القسم', callback_data='add_section')
        btn3 = telebot.types.InlineKeyboardButton(text='تغير الاسم', callback_data='add_candidate')
        btn4 = telebot.types.InlineKeyboardButton(text='لا', callback_data='non_delet')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "هل تريد تغير شىء او الغاء العملية ✅",reply_markup=keyboard)
    elif call.data == "non_delet":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "تم الغاء التوثيق ✅")
        user_list1.clear()
    elif call.data == "section":
        ref = db.reference(f'/section')
        user_data = ref.get()
        if user_data is None:
            bot.send_message(chat_id,"عذرًا، لا يوجد قسم. الرجاء إضافة قسم ثم قم بإضافة متسابق.⛔️")
            return
        else:
            if not section:
                for x in user_data:
                    section.append(x)
            KeyButton = InlineKeyboardMarkup()
            for sec in section:
                KeyButton.add(InlineKeyboardButton(text = sec, callback_data=f"sec_{sec}"))
                coun+=1
            bot.send_message(chat_id,"اخنر قسم من الاقسام الاتيه 🗂",reply_markup=KeyButton)
    elif call.data == "change_icon1":
        try:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔥", callback_data="icon_🔥"))
            markup.add(InlineKeyboardButton("❤️", callback_data="icon_❤️"))
            if emoji_list:
                for emoji in emoji_list:
                    markup.add(InlineKeyboardButton(f"{emoji}", callback_data=f"icon_{emoji}"))
                markup.add(InlineKeyboardButton(f"حذف ايقونة 🗑", callback_data=f"dlet_icon"))    
            markup.add(InlineKeyboardButton("إضافة ايقونة جديده 📥", callback_data="add_icon"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "🔄 اختر الأيقونة الجديدة:",reply_markup=markup)
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء تغيير الأيقونة: {e}")
        # else:
        #     bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحيات تغيير الأيقونة.")
    elif call.data == "add_icon":
        mse = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "الرجاء ارسال الايقونة التي تريد اضافتها ➕ \nملاحظة يمكنك ارسال ايموجي فقط")
        bot.register_next_step_handler(mse, tset_emoje)
    elif call.data == "dlet_icon":
        try:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("🔥", callback_data="delicon_🔥"))
            markup.add(InlineKeyboardButton("❤️", callback_data="delicon_❤️"))
            if emoji_list:
                for emoji in emoji_list:
                    markup.add(InlineKeyboardButton(f"{emoji}", callback_data=f"delicon_{emoji}"))
                markup.add(InlineKeyboardButton(f"حذف ايقونة 🗑", callback_data=f"dlet_icon"))    
            markup.add(InlineKeyboardButton("إضافة ايقونة جديده 📥", callback_data="add_icon"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "🔄 اختر الأيقونة لحذفها:",reply_markup=markup)
        except Exception as e:
            bot.send_message(call.message.chat.id, f"حدث خطأ أثناء تغيير الأيقونة: {e}")
    elif call.data == "dlet_sec":
        coun = 0
        if not section:
            bot.send_message(chat_id,"عذرًا، لا يوجد قسم. الرجاء إضافة قسم ثم قم بإضافة متسابق.⛔️")
            return
        else:
            KeyButton = InlineKeyboardMarkup()
            for sec in section:
                KeyButton.add(InlineKeyboardButton(text = f"{sec} 🗑", callback_data=f"dlesec_{coun}"))
                coun+=1
            KeyButton.add(InlineKeyboardButton(text = f"رجوع", callback_data=f"alkama"))
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "اخنر قسم من الاقسام الاتيه لحذفه 🗂",reply_markup=KeyButton)
    elif call.data == "alkama":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("➕ إضافة متسابق", callback_data="add_candidate"))
        markup.add(InlineKeyboardButton(f"🔄 تغيير أيقونة التصويت (حاليًا: {vote_icon[0]})", callback_data="change_icon1"))
        markup.add(InlineKeyboardButton("حذف قسم 🗑", callback_data="dlet_sec"))
        markup.add(InlineKeyboardButton("➕ إضافة قسم", callback_data="add_section"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,text = "🔧 لوحة التحكم:",reply_markup=markup)
    elif call.data == "add_tim":
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
        if timers:
            for x in timers:
                keyboard.add(InlineKeyboardButton(f"{x}", callback_data=f"tims_{x}"))
        keyboard.add(InlineKeyboardButton("اضافة وقت اخر", callback_data=f"tim_adde"))    
        # تعديل الرسالة وإضافة لوحة المفاتيح المضمنة
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*متى تريد ان تنتهي المسابقة؟*", parse_mode='Markdown', reply_markup=keyboard)

    elif call.data == "no_tim":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*تم الغاء اضافة الوقت سوف تنتهي المسابقة بعد الضغط على ايقاف المسابقة*",parse_mode='Markdown')
    elif call.data == "tim_adde":
        mes1 = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"*الرجاء ارسال الوقت بساعة والدقيقه مثل على ذلك\n12:00*",parse_mode='Markdown')
        bot.register_next_step_handler(mes1, add_tiemr)
    elif call.data == "tiemard":
        show_remaining_time(chat_id,call)
    elif call.data == "tameas":
        pass 
@bot.message_handler(func=lambda message: message.from_user.id in banned_users)
def handle_banned_users(message):
    bot.send_message(message.chat.id, "🚫 حسابك محظور من استخدام هذا البوت.")
bot.infinity_polling()