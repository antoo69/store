from aiogram import types, Router
from database import get_products, get_product_by_id

router = Router()

@router.callback_query(lambda callback: callback.data == "produk")
async def show_products(callback: types.CallbackQuery):
    products = get_products()
    if not products:
        await callback.message.edit_text("⚠️ Tidak ada produk tersedia.")
        return

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text=product["name"], callback_data=f"product_{product['id']}")]
        for product in products
    ])

    await callback.message.edit_text("🛒 Pilih produk:", reply_markup=keyboard)

@router.callback_query(lambda callback: callback.data.startswith("product_"))
async def show_product_detail(callback: types.CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    product = get_product_by_id(product_id)

    if product:
        text = f"📌 **{product['name']}**\n💰 Harga: {product['price']}\n📖 Deskripsi: {product['description']}"
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="🔙 Kembali", callback_data="produk")]
        ])
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")
    else:
        await callback.message.edit_text("⚠️ Produk tidak ditemukan.")
