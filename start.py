from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, MessageNotModified
import asyncio
from bot import app
from config import OWNER_USERNAME as OWNER_NAME # Changed to use correct config variable

CTYPE = enums.ChatType

# Tombol utama untuk /start
start_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Tambahkan ke Group", url="http://t.me/FsAnkesBot?startgroup=true")],
    [InlineKeyboardButton("🛍️ Produk", callback_data="produk")],
    [InlineKeyboardButton("💰 Harga", callback_data="harga")],
    [InlineKeyboardButton("⚙️ Menu Bot", callback_data="menu")]
])

# Handler untuk perintah /start
@app.on_message(filters.command("start") & filters.private | filters.group)
async def start_msg(client, message):
    try:
        user = message.from_user.mention
        chat_type = message.chat.type

        if chat_type == CTYPE.PRIVATE:
            msg = f"👋 Hi {user}! Saya bot anti-spam. Pilih menu di bawah 👇"
            await message.reply_text(msg, reply_markup=start_keyboard)

        elif chat_type in [CTYPE.GROUP, CTYPE.SUPERGROUP]:
            msg = f"👋 Hi! Jadikan saya admin untuk menghapus spam. - {OWNER_NAME}"
            await message.reply_text(msg)
    except Exception as e:
        print(f"Error in start_msg: {str(e)}")

# Callback handler untuk tombol produk
@app.on_callback_query(filters.regex("^produk$"))
async def produk_callback(client, callback_query: CallbackQuery):
    try:
        await callback_query.answer()
        text = """🛍️ Daftar Produk Kami:
    
1. Produk A - Deskripsi singkat
2. Produk B - Deskripsi singkat
3. Produk C - Deskripsi singkat"""
        await callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_start")
        ]]))
    except MessageNotModified:
        pass
    except Exception as e:
        print(f"Error in produk_callback: {str(e)}")

# Callback handler untuk tombol harga  
@app.on_callback_query(filters.regex("^harga$"))
async def harga_callback(client, callback_query: CallbackQuery):
    try:
        await callback_query.answer()
        text = """💰 Daftar Harga:
    
• Produk A: Rp xxx.xxx
• Produk B: Rp xxx.xxx
• Produk C: Rp xxx.xxx"""
        await callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_start")
        ]]))
    except MessageNotModified:
        pass
    except Exception as e:
        print(f"Error in harga_callback: {str(e)}")

# Callback handler untuk menu bot
@app.on_callback_query(filters.regex("^menu$"))
async def menu_callback(client, callback_query: CallbackQuery):
    try:
        await callback_query.answer()
        text = """⚙️ Menu Bot:

/start - Mulai bot
/help - Bantuan
/about - Tentang bot"""
        await callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_start")
        ]]))
    except MessageNotModified:
        pass
    except Exception as e:
        print(f"Error in menu_callback: {str(e)}")

# Callback handler untuk tombol kembali
@app.on_callback_query(filters.regex("^back_to_start$"))
async def back_to_start(client, callback_query: CallbackQuery):
    try:
        await callback_query.answer()
        user = callback_query.from_user.mention
        msg = f"👋 Hi {user}! Saya bot anti-spam. Pilih menu di bawah 👇"
        await callback_query.message.edit_text(msg, reply_markup=start_keyboard)
    except MessageNotModified:
        pass
    except Exception as e:
        print(f"Error in back_to_start: {str(e)}")

print("✅ start.py loaded")
