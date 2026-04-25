from info import *
from Classes import *
comm = Command_handln()
@bot.message_handler(commands=["start","help","id",'kick', 'ban', 'unban', 'mute', 'unmute',"info","warn","lock","unlock","rules","members"])
def hndle(message):
    comm.handle_user(message)
bot.infinity_polling()