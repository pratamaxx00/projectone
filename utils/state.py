from telegram.ext import ConversationHandler

# State untuk mengganti pengaturan
SET_BOT_NAME, SET_BOT_PHOTO, SET_BOT_ABOUT, SET_WELCOME_MSG = range(4)

def cancel_keyboard():
    from telegram import ReplyKeyboardMarkup
    return ReplyKeyboardMarkup([["🔙 Kembali"]], resize_keyboard=True)
