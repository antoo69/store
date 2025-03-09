from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

app = Client("store_bot")

# Daftar produk langsung dalam kode
products = [
    {"id": "1", "name": "Produk A", "description": "Deskripsi Produk A", "price": "Rp100.000"},
    {"id": "2", "name": "Produk B", "description": "Deskripsi Produk B", "price": "Rp200.000"},
    {"id": "3", "name": "Produk C", "description": "Deskripsi Produk C", "price": "Rp300.000"},
]

OWNER_USERNAME = "admin_store"  # Ganti dengan username admin

@app.on_message(filters.command("start"))
def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛍 Produk", callback_data="produk")],
        [InlineKeyboardButton("📖 Cara Order", callback_data="cara_order")],
        [InlineKeyboardButton("💰 Harga", callback_data="harga")]
    ])
    
    text = "👋 Selamat datang di *Store Bot*\!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order\."
    message.reply(text, reply_markup=keyboard, parse_mode="markdownV2")

@app.on_callback_query(filters.regex("^produk$"))
def show_products(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton(product["name"], callback_data=f"product_{product['id']}")]
                for product in products]
    keyboard.append([InlineKeyboardButton("🔙 Kembali ke Menu", callback_data="back_to_menu")])
    
    callback_query.message.edit("🛒 Pilih produk:", reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("^product_\d+$"))
def show_product_details(client, callback_query: CallbackQuery):
    product_id = callback_query.data.split("_")[1]
    product = next((p for p in products if p["id"] == product_id), None)
    
    if not product:
        callback_query.answer("⚠️ Produk tidak ditemukan.", show_alert=True)
        return
    
    text = f"📌 *{product['name']}*\n\n📝 {product['description']}\n💰 Harga: *{product['price']}*"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Order Sekarang", url=f"https://t.me/{OWNER_USERNAME}?text=Halo,%20saya%20ingin%20order%20{product['name']}")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="produk")]
    ])
    
    callback_query.message.edit(text, reply_markup=keyboard, parse_mode="markdownV2")

@app.on_callback_query(filters.regex("^cara_order$"))
def cara_order(client, callback_query: CallbackQuery):
    text = "📖 *Cara Order:*\n1️⃣ Pilih produk yang ingin dibeli\n2️⃣ Klik tombol 'Order Sekarang'\n3️⃣ Kirim pesan ke admin dan lakukan pembayaran\n4️⃣ Tunggu konfirmasi dan pengiriman"
    callback_query.message.edit(text, parse_mode="markdownV2", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_menu")]
    ]))

@app.on_callback_query(filters.regex("^harga$"))
def harga(client, callback_query: CallbackQuery):
    text = "💰 Harga produk bervariasi\. Hubungi admin untuk info lebih lanjut\."
    callback_query.message.edit(text, parse_mode="markdownV2", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_menu")]
    ]))

@app.on_callback_query(filters.regex("^back_to_menu$"))
def back_to_menu(client, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛍 Produk", callback_data="produk")],
        [InlineKeyboardButton("📖 Cara Order", callback_data="cara_order")],
        [InlineKeyboardButton("💰 Harga", callback_data="harga")]
    ])
    callback_query.message.edit("👋 Selamat datang di *Store Bot*\!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order\.", 
                                reply_markup=keyboard, parse_mode="markdownV2")

app.run()
