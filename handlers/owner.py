from telegram import Update, InputFile
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, CommandHandler, filters
from utils.auth import get_user_role
from utils.state import SET_BOT_NAME, SET_BOT_PHOTO, SET_BOT_ABOUT, SET_WELCOME_MSG, cancel_keyboard

async def owner_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    role = get_user_role(update.effective_user.id)
    if role != "owner":
        await update.message.reply_text("❌ Fitur ini hanya untuk owner.")
        return ConversationHandler.END

    keyboard = [["Ganti Nama Bot", "Ganti Foto Bot"], ["Ganti Deskripsi", "Ganti Welcome"], ["🔙 Kembali"]]
    from telegram import ReplyKeyboardMarkup
    await update.message.reply_text("⚙️ Panel Owner:\nSilakan pilih pengaturan:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def set_bot_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Silakan kirim nama baru bot:", reply_markup=cancel_keyboard())
    return SET_BOT_NAME

async def receive_bot_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_my_name(name=update.message.text)
    await update.message.reply_text("✅ Nama bot berhasil diganti.")
    return ConversationHandler.END

async def set_bot_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🖼️ Kirim foto baru bot:", reply_markup=cancel_keyboard())
    return SET_BOT_PHOTO

async def receive_bot_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        await context.bot.set_chat_photo(chat_id=update.effective_chat.id, photo=await photo_file.download_to_drive())
        await update.message.reply_text("✅ Foto bot berhasil diganti.")
    else:
        await update.message.reply_text("❌ Tolong kirim foto, bukan teks.")
    return ConversationHandler.END

async def set_bot_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Kirim deskripsi bot baru (about):", reply_markup=cancel_keyboard())
    return SET_BOT_ABOUT

async def receive_bot_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_my_description(description=update.message.text)
    await update.message.reply_text("✅ Deskripsi berhasil diperbarui.")
    return ConversationHandler.END

async def set_welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot_data["welcome"] = update.message.text
    await update.message.reply_text("✅ Pesan sambutan berhasil diperbarui.")
    return ConversationHandler.END

async def welcome_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 Kirim pesan sambutan baru:", reply_markup=cancel_keyboard())
    return SET_WELCOME_MSG

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Dibatalkan.", reply_markup=None)
    return ConversationHandler.END
