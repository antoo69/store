from aiogram import types
from bot import dp
from database import get_products, get_product_by_id
from config import OWNER_ID

@dp.message_handler(lambda message: message.text == "🛍 Produk")
async def show_products(message: types.Message):
    products = get_products()
    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(types.InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}'))
    
    await message.answer("🔽 Pilih produk yang ingin diorder:", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data.startswith('product_'))
async def product_detail(call: types.CallbackQuery):
    product_id = call.data.split('_')[1]
    product = get_product_by_id(product_id)
    
    text = f"📌 *{product[0]}*\n💰 Harga: {product[1]}\n📖 Deskripsi: {product[2]}"
    keyboard = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🛒 Order Sekarang", url=f"https://t.me/{OWNER_ID}?text=Saya ingin order {product[0]}")
    )
    
    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "📖 Cara Order")
async def order_guide(message: types.Message):
    text = "🛒 *Cara Order:*\n1️⃣ Pilih produk yang ingin dibeli\n2️⃣ Klik tombol 'Order Sekarang'\n3️⃣ Kirim pesan ke admin dan lakukan pembayaran\n4️⃣ Tunggu konfirmasi dan pengiriman"
    await message.answer(text, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "💰 Harga")
async def price_list(message: types.Message):
    products = get_products()
    
    text = "💰 *Daftar Harga:*\n"
    for product in products:
        text += f"- {product[0]}: {product[1]}\n"
    
    await message.answer(text, parse_mode="Markdown")
