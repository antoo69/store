from aiogram import types, Router
from aiogram.filters import Command
from database import get_products, get_product_by_id

router = Router()

# Handler untuk tombol Produk
@router.callback_query(lambda call: call.data == "produk")
async def show_products(call: types.CallbackQuery):
    products = get_products()
    if not products:
        await call.message.answer("⚠️ Tidak ada produk tersedia.")
        return
    
    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(types.InlineKeyboardButton(
            text=product["name"], callback_data=f"product_{product['id']}"
        ))

    await call.message.answer("🛒 Pilih produk:", reply_markup=keyboard)
    await call.answer()

# Handler untuk tombol Cara Order
@router.callback_query(lambda call: call.data == "cara_order")
async def cara_order(call: types.CallbackQuery):
    text = "📖 *Cara Order:*\n1️⃣ Pilih produk yang ingin dibeli\n2️⃣ Klik tombol 'Order Sekarang'\n3️⃣ Kirim pesan ke admin dan lakukan pembayaran\n4️⃣ Tunggu konfirmasi dan pengiriman"
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# Handler untuk tombol Harga
@router.callback_query(lambda call: call.data == "harga")
async def harga(call: types.CallbackQuery):
    await call.message.answer("💰 Harga produk bervariasi. Hubungi admin untuk info lebih lanjut.")
    await call.answer()
