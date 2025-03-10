from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import OWNER_USERNAME

# Teks sambutan
START_TEXT = (
    "👋 Selamat datang di *Shop Bot*!\n\n"
    "🛍️ Jelajahi katalog kami dan buat pesanan dengan mudah.\n"
    "📦 Gunakan tombol di bawah untuk mulai belanja!"
)

# Keyboard Menu Utama
START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🛍️ Catalog", callback_data="view_catalog")],
    [InlineKeyboardButton("🛒 Cart", callback_data="view_cart")],
    [
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
        InlineKeyboardButton("📦 Orders", callback_data="orders")
    ],
    [InlineKeyboardButton("👨‍💻 Contact Admin", url=f"https://t.me/{OWNER_USERNAME}")]
])

# Handler untuk perintah /start
async def start_command(client: Client, message: Message):
    await message.reply_text(
        START_TEXT,
        reply_markup=START_KEYBOARD,
        parse_mode="markdown"
    )
