import logging
import asyncio
from datetime import datetime, timedelta
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pytz import timezone

# ------------------ الإعدادات الأساسية ------------------
TOKEN = "7399603010:AAEls8X-6KjwitR3vfwoUu0B3ip8gtHfbqA"
CHANNEL_ID = "@Qran_krem_1"
ADMINS = [984370413]
TIMEZONE = timezone("Africa/Tripoli")
INTERVAL_SECONDS = 15
MAX_BATCH_SIZE = 20

# ------------------ نظام التخزين المتقدم ------------------
class AdvancedStorage:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.processed_count = 0
        self.lock = asyncio.Lock()
        self.last_processed = datetime.now(TIMEZONE)

storage = AdvancedStorage()

# ------------------ إعداد المخطط ------------------
scheduler = AsyncIOScheduler()

# ------------------ معالجة الدفعات ------------------
async def process_batch(context: CallbackContext):
    try:
        current_batch = []
        async with storage.lock:
            for _ in range(MAX_BATCH_SIZE):
                if not storage.queue.empty():
                    current_batch.append(await storage.queue.get())
        
        if not current_batch:
            return

        success_count = 0
        bot = context.bot
        for item in current_batch:
            try:
                if item['type'] == 'photo':
                    await bot.send_photo(
                        chat_id=CHANNEL_ID,
                        photo=item['content'],
                        caption=item.get('caption', '')
                    )
                elif item['type'] == 'video':
                    await bot.send_video(
                        chat_id=CHANNEL_ID,
                        video=item['content'],
                        caption=item.get('caption', ''),
                        duration=item.get('duration', 0)
                    )
                elif item['type'] == 'text':
                    await bot.send_message(
                        chat_id=CHANNEL_ID,
                        text=item['content']
                    )
                success_count += 1
            except Exception as e:
                logging.error(f"Failed to send item: {str(e)}")
                await storage.queue.put(item)

        async with storage.lock:
            storage.processed_count += success_count
            storage.last_processed = datetime.now(TIMEZONE)

        await send_status_update(bot, success_count, len(current_batch))
        
    except Exception as e:
        logging.error(f"Batch processing error: {str(e)}")
        await context.bot.send_message(ADMINS[0], f"🚨 Critical Error: {str(e)}")

async def send_status_update(bot: Bot, success: int, total: int):
    status_report = (
        f"📦 تقرير الدفعة\n"
        f"النجاح: {success}/{total}\n"
        f"في قائمة الانتظار: {storage.queue.qsize()}\n"
        f"إجمالي المعالَج: {storage.processed_count}"
    )
    await bot.send_message(ADMINS[0], status_report)

# ------------------ معالجة المدخلات ------------------
async def handle_input(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        if user.id not in ADMINS:
            return

        content = await extract_content(update)
        if not content:
            return

        await storage.queue.put(content)
        await send_instant_feedback(update)

    except Exception as e:
        logging.error(f"Input handling error: {str(e)}")
        await update.message.reply_text("⚠️ فشل في معالجة المحتوى")

async def extract_content(update: Update):
    content = {}
    if update.message.photo:
        content = {
            'type': 'photo',
            'content': update.message.photo[-1].file_id,
            'caption': update.message.caption,
            'timestamp': datetime.now(TIMEZONE)
        }
    elif update.message.video:
        content = {
            'type': 'video',
            'content': update.message.video.file_id,
            'caption': update.message.caption,
            'duration': update.message.video.duration,
            'timestamp': datetime.now(TIMEZONE)
        }
    elif update.message.text:
        content = {
            'type': 'text',
            'content': update.message.text,
            'timestamp': datetime.now(TIMEZONE)
        }
    return content

async def send_instant_feedback(update: Update):
    feedback = (
        f"✅ تم الاستلام بنجاح\n"
        f"الرقم التسلسلي: {storage.processed_count + storage.queue.qsize() + 1}"
    )
    await update.message.reply_text(feedback)

# ------------------ لوحة التحكم ------------------
async def control_panel(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton("📊 حالة النظام"), KeyboardButton("🔄 تحديث القوائم")],
        [KeyboardButton("⚙️ الإعدادات"), KeyboardButton("📤 تفريغ قائمة الانتظار")]
    ]
    await update.message.reply_text(
        "🖥️ لوحة التحكم الرئيسية:",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

# ------------------ إدارة النظام ------------------
async def system_status(update: Update, context: CallbackContext):
    status = (
        f"📈 إحصائيات النظام:\n"
        f"• المعالَج: {storage.processed_count}\n"
        f"• في الانتظار: {storage.queue.qsize()}\n"
        f"• آخر معالجة: {storage.last_processed.strftime('%Y-%m-%d %H:%M:%S')}"
    )
    await update.message.reply_text(status)

# ------------------ التشغيل الرئيسي ------------------
async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", control_panel))
    application.add_handler(MessageHandler(filters.ALL, handle_input))
    application.add_handler(MessageHandler(filters.Regex("^📊 حالة النظام$"), system_status))

    scheduler.add_job(
        process_batch,
        'interval',
        seconds=INTERVAL_SECONDS,
        args=[application],
        timezone=TIMEZONE
    )
    scheduler.start()
    
    await application.run_polling()

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
        ]
    )
    
    asyncio.run(main())