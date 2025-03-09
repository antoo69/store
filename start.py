from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, MessageNotModified
import asyncio
from bot import app  # Gunakan app dari bot.py
from config import OWNER_NAME

CTYPE = enums.ChatType

# Tombol utama untuk /start
start_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Tambahkan ke Group", url="http://t.me/FsAnkesBot?startgroup=true")],
    [InlineKeyboardButton("👮 Owner", url=f"http://t.me/{OWNER_NAME}")],
    [InlineKeyboardButton("💬 Support", url="https://t.me/FerdiSupport")],
    [InlineKeyboardButton("⚙️ Menu Bot", callback_data="menu")]
])

# Handler untuk perintah /start
@app.on_message(filters.command("start"))
async def start_msg(client, message):
    user = message.from_user.mention
    chat_type = message.chat.type

    if chat_type == CTYPE.PRIVATE:
        msg = f"👋 Hi {user}! Saya bot anti-spam. Pilih menu di bawah 👇"
        await message.reply_text(msg, reply_markup=start_keyboard)

    elif chat_type in [CTYPE.GROUP, CTYPE.SUPERGROUP]:
        msg = f"👋 Hi! Jadikan saya admin untuk menghapus spam. - {OWNER_NAME}"
        await message.reply_text(msg)

print("✅ start.py loaded")
