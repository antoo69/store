from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database import get_products, get_product_by_id
from config import OWNER_USERNAME

router = Router()

@router.message(F.text == "🛍 Produk")
async def show_products(message: Message):
    products = get_products()
    
    # Pastikan ada produk dalam database
    if not products:
        await message.answer("⚠️ Belum ada produk yang tersedia.")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}')] for product in products
    ])

    await message.answer("🔽 Pilih produk yang ingin diorder:", reply_markup=keyboard)

@router.callback_query(F.data.startswith("product_"))
async def product_detail(call: CallbackQuery):
    product_id = call.data.split('_')[1]
    product = get_product_by_id(product_id)

    # Cek apakah produk ada dalam database
    if not product:
        await call.answer("❌ Produk tidak ditemukan!", show_alert=True)
        return

    text = f"📌 *{product[0]}*\n💰 Harga: {product[1]}\n📖 Deskripsi: {product[2]}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🛒 Order Sekarang", url=f"https://t.me/{OWNER_USERNAME}?text=Saya ingin order {product[0]}")]
    ])

    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=keyboard)

@router.message(F.text == "📖 Cara Order")
async def order_guide(message: Message):
    text = (
        "🛒 *Cara Order:*\n"
        "1️⃣ Pilih produk yang ingin dibeli\n"
        "2️⃣ Klik tombol 'Order Sekarang'\n"
        "3️⃣ Kirim pesan ke admin dan lakukan pembayaran\n"
        "4️⃣ Tunggu konfirmasi dan pengiriman"
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text == "💰 Harga")
async def price_list(message: Message):
    products = get_products()

    # Pastikan ada produk sebelum mengirim daftar harga
    if not products:
        await message.answer("⚠️ Belum ada daftar harga yang tersedia.")
        return

    text = "💰 *Daftar Harga:*\n"
    for product in products:
        text += f"- {product[0]}: {product[1]}\n"

    await message.answer(text, parse_mode="Markdown")
