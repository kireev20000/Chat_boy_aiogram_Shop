import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

#Список Админов ID
ADMINS = []