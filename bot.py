from pyrogram import Client
from config import TOKEN

# Initialize bot instance
app = Client(
    name="store_bot",
    bot_token=TOKEN
)
