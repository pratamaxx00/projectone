from telegram import ReplyKeyboardMarkup

def start_keyboard(role="user"):
    if role == "owner":
        keyboard = [
            ["📚 Catatan", "📁 Folder"],
            ["👥 Kelola User", "📂 Akses File"],
            ["⚙️ Owner Panel"]
        ]
    elif role == "admin":
        keyboard = [
            ["📚 Catatan", "📁 Folder"],
            ["👥 Kelola User", "📂 Akses File"]
        ]
    else:  # user biasa
        keyboard = [
            ["📚 Catatan", "📁 Folder"],
            ["ℹ️ Bantuan"]
        ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
