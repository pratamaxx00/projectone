import os
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = int(os.getenv("OWNER_ID"))
ADMINS = list(map(int, os.getenv("ADMINS", "").split(","))) if os.getenv("ADMINS") else []

def get_user_role(user_id: int) -> str:
    if user_id == OWNER_ID:
        return "owner"
    elif user_id in ADMINS:
        return "admin"
    else:
        return "user"
