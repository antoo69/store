from pyrogram import Client
from config import BOT_TOKEN

# Initialize bot instance
app = Client(
    name="store_bot",
    bot_token=BOT_TOKEN
)
