from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import OWNER_USERNAME

# Tombol menu awal
START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🛍️ Catalog", callback_data="view_catalog")],
    [InlineKeyboardButton("🛒 Cart", callback_data="view_cart")],
    [
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
        InlineKeyboardButton("📦 Orders", callback_data="orders")
    ],
    [InlineKeyboardButton("👨‍💻 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]
])

# Handler untuk /start
async def start_command(client: Client, message: Message):
    await message.reply_text(
        "Welcome to our Shop Bot! 🎉\n"
        "Browse our catalog and make your purchase easily.",
        reply_markup=START_KEYBOARD
    )
