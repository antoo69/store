from aiogram import types, Router
from aiogram.filters import Command

router = Router()

# Daftar produk langsung dalam kode
products = [
    {"id": "1", "name": "Produk A", "description": "Deskripsi Produk A", "price": "Rp100.000"},
    {"id": "2", "name": "Produk B", "description": "Deskripsi Produk B", "price": "Rp200.000"},
    {"id": "3", "name": "Produk C", "description": "Deskripsi Produk C", "price": "Rp300.000"},
]

OWNER_USERNAME = "admin_store"  # Ganti dengan username admin

# /start command
@router.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🛍 Produk", callback_data="produk")],
        [types.InlineKeyboardButton(text="📖 Cara Order", callback_data="cara_order")],
        [types.InlineKeyboardButton(text="💰 Harga", callback_data="harga")]
    ])

    text = "👋 Selamat datang di *Store Bot*\!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order\."
    await message.answer(text, reply_markup=keyboard, parse_mode="MarkdownV2")

# Callback untuk menampilkan daftar produk
@router.callback_query(lambda call: call.data == "produk")
async def show_products(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(types.InlineKeyboardButton(
            text=product["name"], callback_data=f"product_{product['id']}"
        ))
    keyboard.add(types.InlineKeyboardButton("🔙 Kembali ke Menu", callback_data="back_to_menu"))

    await call.message.edit_text("🛒 Pilih produk:", reply_markup=keyboard)

# Callback untuk menampilkan detail produk
@router.callback_query(lambda call: call.data.startswith("product_"))
async def show_product_details(call: types.CallbackQuery):
    product_id = call.data.split("_")[1]
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        await call.answer("⚠️ Produk tidak ditemukan.", show_alert=True)
        return

    text = f"📌 *{product['name']}*\n\n📝 {product['description']}\n💰 Harga: *{product['price']}*"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton("🛒 Order Sekarang", url=f"https://t.me/{OWNER_USERNAME}?text=Halo,%20saya%20ingin%20order%20{product['name']}")],
        [types.InlineKeyboardButton("🔙 Kembali", callback_data="produk")]
    ])

    await call.message.edit_text(text, reply_markup=keyboard, parse_mode="MarkdownV2")

# Callback untuk cara order
@router.callback_query(lambda call: call.data == "cara_order")
async def cara_order(call: types.CallbackQuery):
    text = "📖 *Cara Order:*\n1️⃣ Pilih produk yang ingin dibeli\n2️⃣ Klik tombol 'Order Sekarang'\n3️⃣ Kirim pesan ke admin dan lakukan pembayaran\n4️⃣ Tunggu konfirmasi dan pengiriman"
    await call.message.edit_text(text, parse_mode="MarkdownV2", reply_markup=types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton("🔙 Kembali", callback_data="back_to_menu")]]
    ))

# Callback untuk harga
@router.callback_query(lambda call: call.data == "harga")
async def harga(call: types.CallbackQuery):
    text = "💰 Harga produk bervariasi\. Hubungi admin untuk info lebih lanjut\."
    await call.message.edit_text(text, parse_mode="MarkdownV2", reply_markup=types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton("🔙 Kembali", callback_data="back_to_menu")]]
    ))

# Callback untuk kembali ke menu utama
@router.callback_query(lambda call: call.data == "back_to_menu")
async def back_to_menu(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🛍 Produk", callback_data="produk")],
        [types.InlineKeyboardButton(text="📖 Cara Order", callback_data="cara_order")],
        [types.InlineKeyboardButton(text="💰 Harga", callback_data="harga")]
    ])
    await call.message.edit_text("👋 Selamat datang di *Store Bot*\!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order\.", reply_markup=keyboard, parse_mode="MarkdownV2")
