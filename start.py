from aiogram import types, Router
from aiogram.filters import Command
from database import get_products, get_product_by_id

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🛍 Produk", "📖 Cara Order", "💰 Harga")

    text = "👋 Selamat datang di Store Bot!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order."
    await message.answer(text, reply_markup=keyboard)

@router.message(lambda message: message.text == "🛍 Produk")
async def show_products(message: types.Message):
    products = get_products()
    if not products:
        await message.answer("⚠️ Tidak ada produk tersedia.")
        return
    
    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(types.InlineKeyboardButton(
            text=product["name"], callback_data=f"product_{product['id']}"
        ))

    await message.answer("🛒 Pilih produk:", reply_markup=keyboard)

@router.callback_query(lambda call: call.data.startswith("product_"))
async def show_product_detail(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[1])
    product = get_product_by_id(product_id)

    if product:
        text = f"📌 **{product['name']}**\n💰 Harga: {product['price']}\n📖 Deskripsi: {product['description']}"
        await call.message.answer(text)
    else:
        await call.message.answer("⚠️ Produk tidak ditemukan.")

