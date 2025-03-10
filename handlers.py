from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from database import get_catalog, add_to_cart, get_cart
from start import START_KEYBOARD  # Pastikan ini ada jika digunakan

async def start_command(client: Client, message: Message):
    await message.reply_text(
        "Welcome to our Shop Bot! 🎉\n"
        "Browse our catalog and make your purchase easily.",
        reply_markup=START_KEYBOARD
    )

async def catalog_callback(client: Client, callback_query: CallbackQuery):
    catalog = await get_catalog()
    if not catalog:
        await callback_query.message.edit_text("Katalog kosong.")
        return
    # Tambahkan logika untuk menampilkan katalog

def register_handlers(app: Client):
    app.add_handler(filters.command("start") & filters.private, start_command)  # ✅ Fix
    app.add_handler(filters.regex("^catalog$"), catalog_callback)  # ✅ Fix
