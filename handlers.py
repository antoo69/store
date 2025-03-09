from aiogram import types, Router
from aiogram.filters import Command
from config import owner_username  # Mengambil username owner dari config

router = Router()

# Daftar Produk (bisa langsung diedit di sini)
PRODUCTS = [
    {"id": "1", "name": "iPhone 14", "price": "Rp 15.000.000", "description": "Smartphone terbaru dengan chip A16 Bionic."},
    {"id": "2", "name": "MacBook Air M2", "price": "Rp 20.000.000", "description": "Laptop ringan dengan performa tinggi dan baterai tahan lama."},
    {"id": "3", "name": "Apple Watch Series 8", "price": "Rp 7.000.000", "description": "Smartwatch canggih dengan fitur kesehatan terbaru."},
]

# Tombol kembali ke daftar produk
back_to_menu_keyboard = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton("🔙 Kembali", callback_data="produk")
)

# Handler untuk menampilkan daftar produk
@router.callback_query(lambda query: query.data == "produk")
async def show_products(query: types.CallbackQuery):
    if not PRODUCTS:
        await query.edit_message_text("⚠️ Tidak ada produk tersedia.")
        return

    keyboard = types.InlineKeyboardMarkup()
    for product in PRODUCTS:
        keyboard.add(types.InlineKeyboardButton(
            text=product["name"], callback_data=f"product_{product['id']}"
        ))

    await query.edit_message_text("🛒 Pilih produk:", reply_markup=keyboard)

# Handler untuk menampilkan detail produk
@router.callback_query(lambda query: query.data.startswith("product_"))
async def show_product_detail(query: types.CallbackQuery):
    product_id = query.data.split("_")[1]
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)

    if not product:
        await query.answer("⚠️ Produk tidak ditemukan.", show_alert=True)
        return

    text = f"""<b>📦 {product['name']}</b>
💰 <b>Harga:</b> {product['price']}
📝 <b>Deskripsi:</b> {product['description']}"""

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text="🛒 Order Sekarang",
            url=f"https://t.me/{owner_username}?text=Order%20{product['name']}%20dengan%20username%20@yourusername"
        ),
        types.InlineKeyboardButton(
            text="🔙 Kembali",
            callback_data="produk"
        )
    )

    await query.edit_message_text(text, parse_mode="HTML", reply_markup=keyboard)
