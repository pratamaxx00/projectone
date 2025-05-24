import os
from dotenv import load_dotenv
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ConversationHandler, filters
)

# Load .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Cek apakah token terbaca
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN tidak ditemukan. Pastikan file .env sudah ada dan berisi BOT_TOKEN=...")

# Buat bot instance
application = Application.builder().token(BOT_TOKEN).build()

# === Import Handler Modular ===
from handlers.start import start_handler
from handlers.owner import (
    owner_panel, set_bot_name, receive_bot_name,
    set_bot_photo, receive_bot_photo,
    set_bot_about, receive_bot_about,
    set_welcome_message, welcome_input, cancel
)
from utils.state import SET_BOT_NAME, SET_BOT_PHOTO, SET_BOT_ABOUT, SET_WELCOME_MSG

# === Handler Start ===
application.add_handler(CommandHandler("start", start_handler))

# === Handler Owner ===
owner_conv = ConversationHandler(
    entry_points=[
        CommandHandler("owner", owner_panel),
        MessageHandler(filters.Regex("^⚙️ Owner Panel$"), owner_panel),
        MessageHandler(filters.Regex("^Ganti Nama Bot$"), set_bot_name),
        MessageHandler(filters.Regex("^Ganti Foto Bot$"), set_bot_photo),
        MessageHandler(filters.Regex("^Ganti Deskripsi$"), set_bot_about),
        MessageHandler(filters.Regex("^Ganti Welcome$"), welcome_input),
    ],
    states={
        SET_BOT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_bot_name)],
        SET_BOT_PHOTO: [MessageHandler(filters.PHOTO, receive_bot_photo)],
        SET_BOT_ABOUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_bot_about)],
        SET_WELCOME_MSG: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_welcome_message)],
    },
    fallbacks=[MessageHandler(filters.Regex("^🔙 Kembali$"), cancel)],
)
application.add_handler(owner_conv)

# === Jalankan Bot ===
if __name__ == "__main__":
    print("🤖 Bot sedang berjalan... Tekan Ctrl+C untuk keluar.")
    application.run_polling()
