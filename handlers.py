from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
from database import get_catalog, add_to_cart, get_cart
from start import START_KEYBOARD  # Pastikan ini ada jika digunakan

async def start_command(client, message: Message):
    await message.reply_text(
        "Welcome to our Shop Bot! 🎉\n"
        "Browse our catalog and make your purchase easily.",
        reply_markup=START_KEYBOARD
    )

async def catalog_callback(client, callback_query: CallbackQuery):
    catalog = await get_catalog()
    # Handle catalog display logic
    pass

def register_handlers(app: Client):
    app.add_handler(filters.command("start")(start_command))
    app.add_handler(filters.callback_data("catalog")(catalog_callback))
