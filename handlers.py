from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import CallbackQuery
from database import get_catalog
from start import start_command  # 🔥 Import dari start.py

# ✅ Handler untuk menampilkan katalog (Callback)
async def catalog_callback(client: Client, callback_query: CallbackQuery):
    catalog = await get_catalog()
    if not catalog:
        await callback_query.message.edit_text("📦 Katalog masih kosong.")
        return
    await callback_query.message.edit_text("📌 Ini katalog produk kami!")

# ✅ Fungsi untuk mendaftarkan semua handlers
def register_handlers(app: Client):
    app.add_handler(MessageHandler(start_command, filters.command("start") & filters.private))  # 🔥 FIXED
    app.add_handler(CallbackQueryHandler(catalog_callback, filters.regex("^view_catalog$")))  # 🔥 FIXED
