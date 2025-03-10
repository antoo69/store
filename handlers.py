from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import Message, CallbackQuery
from database import get_catalog, add_to_cart, get_cart
from start import start_command  # Import fungsi start_command

# Callback handler untuk katalog
async def catalog_callback(client: Client, callback_query: CallbackQuery):
    catalog = await get_catalog()
    
    if not catalog:
        await callback_query.message.edit_text("📦 Katalog kosong untuk saat ini.")
        return
    
    # Format daftar produk
    catalog_text = "🛍️ *Daftar Produk:*\n\n"
    for product in catalog:
        catalog_text += f"🔹 {product['name']} - 💲{product['price']}\n"
    
    await callback_query.message.edit_text(catalog_text, parse_mode="markdown")

# Fungsi untuk mendaftarkan semua handler
def register_handlers(app: Client):
    # Menangani perintah /start
    app.add_handler(MessageHandler(start_command, filters.command("start") & filters.private))
    
    # Menangani tombol katalog
    app.add_handler(CallbackQueryHandler(catalog_callback, filters.callback_data("view_catalog")))
