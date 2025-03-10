from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME

START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🛍️ Catalog", callback_data="view_catalog")],
    [InlineKeyboardButton("🛒 Cart", callback_data="view_cart")],
    [
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
        InlineKeyboardButton("📦 Orders", callback_data="orders")
    ],
    [InlineKeyboardButton("👨‍💻 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]
])
