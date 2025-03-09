from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Inisialisasi bot
app = Client("store_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
