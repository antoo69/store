from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from bot import app  # Gunakan app dari bot.py
import asyncio
from pyrogram.errors import FloodWait
from config import OWNER_NAME

CTYPE = enums.ChatType

# Tombol utama untuk /start
start_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Tambahkan ke Group", url="http://t.me/FsAnkesBot?startgroup=true")],
    [InlineKeyboardButton("👮 Owner", url=f"http://t.me/{OWNER_NAME}"),
     InlineKeyboardButton("🦖 Store", url="https://t.me/Galerifsyrl")],
    [InlineKeyboardButton("💬 Support", url="https://t.me/FerdiSupport"),
     InlineKeyboardButton("⚙️ Menu Bot", callback_data="menu")],
    [InlineKeyboardButton("✍️Grup", url="https://t.me/+Ox55HJTTsuFiMDY9"),
     InlineKeyboardButton("🎧Music", url="https://t.me/FerdiMusicV1Bot?startgroup=true")]
])

@app.on_message(filters.command("start"))
async def start_msg(client, message: Message):
    print(f"[LOG] Menerima /start dari {message.from_user.id}")  # Debugging
    user = message.from_user.mention
    chat_type = message.chat.type

    if chat_type == CTYPE.PRIVATE:
        msg = f"👋 Hi {user}! Saya Ferdi AntiGcast, siap membantu menghapus spam di grup."
        try:
            await message.reply_photo(photo="https://files.catbox.moe/aggvbq.jpg", caption=msg, reply_markup=start_keyboard)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply_photo(photo="https://files.catbox.moe/aggvbq.jpg", caption=msg, reply_markup=start_keyboard)
    else:
        msg = f"🚀 Tambahkan saya sebagai admin untuk melindungi grup ini dari spam.\n\n👤 Owner: {OWNER_NAME}"
        try:
            await message.reply(text=msg)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=msg)
