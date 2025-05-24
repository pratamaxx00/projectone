from telegram import Update
from telegram.ext import ContextTypes
from utils.buttons import start_keyboard
from utils.auth import get_user_role

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    role = get_user_role(user.id)
    context.user_data["role"] = role

    await update.message.reply_text(
        f"Halo {user.first_name}!\n"
        f"ID Anda: {user.id}\n"
        f"Peran Anda: {role.upper()} ✅\n\n"
        f"Silakan pilih menu di bawah ini:",
        reply_markup=start_keyboard(role)
    )
