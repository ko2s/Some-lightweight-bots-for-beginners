from typing import final
from telegram import Update
from telegram.ext import application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: final = '6538893780:AAEKoGzXwODaYC3OFW3w7IaPck76eTGGlUU'
TOKEN_USERNAME: final = '@Orena_Storebot'


#commands
async def start_command(updare: Update, context:ContextTypes.DEFAULT_TYPE):
    await updare.message.reply_text("مرحبا بك في اورينا")


async def help_command(updare: Update, context:ContextTypes.DEFAULT_TYPE):
    await updare.message.reply_text("يمكنك طلب المساعدة من هنا")


async def custom_command(updare: Update, context:ContextTypes.DEFAULT_TYPE):
    await updare.message.reply_text("The is custom_command!")


#Responses
 
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'مرحبا' in processed:
        return 'مرحبا بك كيف حالك'

    if 'تمام الحمدلله' in processed:
        return 'كيف حال هلك '

    async def error(updare: Update, context:ContextTypes.DEFAULT_TYPE):
        print(f'Update {Update} caused error {context.error}')


if __name__ =='___main___':
    app = application.builder().token(TOKEN).build()

    #Commands
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("custom", custom_command))

#Message
app.add_handler(MessageHandler(filter.TEXT))

