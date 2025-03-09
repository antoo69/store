from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageNotModified
import asyncio
from store import app
from pyrogram import filters, enums
from pyrogram.errors import FloodWait

from config import *

app = Client("store_bot")

CTYPE = enums.ChatType

# Tombol utama untuk /start
start_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ Tambahkan ke Group", url="http://t.me/FsAnkesBot?startgroup=true")
        ],
        [
            InlineKeyboardButton("👮 Owner", url=f"http://t.me/{OWNER_NAME}"),
            InlineKeyboardButton("🦖 Store", url="https://t.me/Galerifsyrl")
        ],
        [
            InlineKeyboardButton("💬 Support", url="https://t.me/FerdiSupport"),
            InlineKeyboardButton("⚙️ Menu Bot", callback_data="menu")
        ],
        [
            InlineKeyboardButton("✍️Grup", url="https://t.me/+Ox55HJTTsuFiMDY9"),
            InlineKeyboardButton("🎧Music", url="https://t.me/FerdiMusicV1Bot?startgroup=true")
        ]
    ]
)

# Tombol utama untuk menu modul
menu_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="📜 Blacklist Word", callback_data="modul_blacklist"),
            InlineKeyboardButton(text="👤 Anti User", callback_data="modul_antiuser")
        ],
        [
            InlineKeyboardButton(text="⏰ Anti Flood", callback_data="modul_antiflood"),
            InlineKeyboardButton(text="🕕 AFK", callback_data="modul_afk")
        ],
        [
            InlineKeyboardButton(text="🗣️ mention", callback_data="modul_tagall"),
            InlineKeyboardButton(text="🦾 AI", callback_data="modul_AI")
        ],
        [
            InlineKeyboardButton(text="💰 Langganan", callback_data="modul_langganan")
        ],
        [
            InlineKeyboardButton("🔙 Kembali ke Awal", callback_data="start")
        ]
    ]
)

# Tombol kembali ke menu
back_to_menu_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🔙 Kembali ke Menu Bot", callback_data="menu")]
    ]
)

# /start handler
@app.on_message(filters.command("start"))
async def start_msg(client, message: Message):
    user = message.from_user.mention
    chat_type = message.chat.type

    if chat_type == CTYPE.PRIVATE:
        msg = f"<blockquote> Hi {user} !\n\nSaya Ferdi AntiGcast, Saya akan membantu Anda untuk menghapus pesan spam di grup Anda. Cara pemakaian ada di tombol menu dibawah 👇👇👇👇:</blockquote>"

        try:
            await message.reply_photo(
                photo="https://files.catbox.moe/aggvbq.jpg",
                caption=msg,
                reply_markup=start_keyboard
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply_photo(
                photo="https://files.catbox.moe/aggvbq.jpg",
                caption=msg,
                reply_markup=start_keyboard
            )

    elif chat_type in [CTYPE.GROUP, CTYPE.SUPERGROUP]:
        msg = f"<blockquote>**Hey!**\n\n__Jadikan saya sebagai admin grup, maka grup ini tidak akan ada spam gcast yang mengganggu!__\n\nCreated by {OWNER_NAME}</blockquote>"
        try:
            await message.reply(text=msg)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=msg)

# Menu utama bot
@app.on_callback_query(filters.regex(r"menu"))
async def menu_callback(client, query: CallbackQuery):
    text = "<blockquote>⚙️ **Menu Bot**\n\nPilih modul untuk mengetahui panduan lengkapnya.</blockquote>"
    try:
        await query.edit_message_text(text=text, reply_markup=menu_keyboard)
    except Exception as e:
        await query.answer(f"Gagal memuat menu: {e}", show_alert=True)

# Callback query untuk kembali ke menu awal (memulai ulang /start)
@app.on_callback_query(filters.regex(r"start_menu"))
async def start_menu_cbq(client, query: CallbackQuery):
    user = query.from_user.mention
    text = f"<blockquote>👋🏻 Hi {user}!\n\nSaya adalah bot anti gcast yang akan membantu Anda untuk menghapus pesan spam di grup Anda. Pilih salah satu tombol di bawah untuk memulai:</blockquote>"

    try:
        # Hapus pesan lama (untuk menghindari pesan yang tidak berubah)
        await query.message.delete()

        # Kirim pesan baru sama seperti /start
        await client.send_photo(
            chat_id=query.message.chat.id,
            photo="https://itzpire.com/file/788e7abe5088.jpg",
            caption=text,
            reply_markup=start_keyboard
        )
    except MessageNotModified:
        # Tangani pesan yang tidak dapat diubah karena tidak ada modifikasi
        await query.answer("Menu sudah berada di kondisi yang sama.", show_alert=True)
    except Exception as e:
        # Tangani error lain yang mungkin muncul
        await query.answer(f"Terjadi kesalahan: {e}", show_alert=True)


# Callback query untuk modul Blacklist Word
@app.on_callback_query(filters.regex(r"modul_blacklist"))
async def blacklist_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>🛑 Modul Blacklist Word

Perintah:
• /bl on/off `<kata>`: Mengaktifkan atau menonaktifkan blacklist word.
• /al `<kata>`: Tambahkan kata ke daftar blacklist.
• /gdl `<kata>`: Hapus kata dari daftar blacklist.
• /wl `<username>`: Untuk menambahkan pengguna ke dalam daftar whitelist (free).
• /unwl `<username>`: Untuk mengeluarkam pengguna dari dalam daftar whitelist.

Fungsi:
- Pesan yang mengandung kata di daftar blacklist otomatis dihapus.
- Gunakan whitelist pada user agar tidak terdeteksi blacklist words.
- Gunakan /wl (username/id) atau reply pengguna untuk memasukan ke dalam daftar whitelist.
</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)

# Callback query untuk modul Anti User
@app.on_callback_query(filters.regex(r"modul_antiuser"))
async def antiuser_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>👤 Modul Anti User

Perintah:
• /dl `<username>`: Blokir pengguna tertentu.
• /ul `<username>`: Hapus pengguna dari database.

Fungsi:
- Semua pesan dari pengguna yang diblokir akan dihapus otomatis.
</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)

# Callback query untuk modul Anti Flood
@app.on_callback_query(filters.regex(r"modul_antiflood"))
async def antiflood_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>⏰ Modul Anti Flood

Perintah:
• /af on/off : Aktifkan atau nonaktifkan anti flood.

Fungsi:
- Mencegah pesan spam yang sama dalam waktu singkat.
</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)

# Callback query untuk modul AFK
@app.on_callback_query(filters.regex(r"modul_afk"))
async def afk_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>🕕 Modul AFK

Perintah:
• /afk `<alasan>`: Aktifkan mode AFK.
• /unafk : Nonaktifkan mode AFK.

Fungsi:
- Menandai pengguna sedang AFK secara otomatis.
</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)
    
@app.on_callback_query(filters.regex(r"modul_AI"))
async def ai_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>🛑 Modul AI 

Perintah:
• /ai : kata kata.
• /ask : kata kata.

</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)

@app.on_callback_query(filters.regex(r"modul_tagall"))
async def tagall_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>🛑 Modul mention/tagall

Perintah:
• /tagall: kata kata atau reply pesan.
• /all : kata kata atau reply pesan.

• /cancel : untuk menghentikan proses tagall.
• /cancelall : untuk menghentikan proses tagall.

</blockquote>"""
    await query.edit_message_text(text=text, reply_markup=back_to_menu_keyboard)

# Callback query untuk modul Langganan
@app.on_callback_query(filters.regex(r"modul_langganan"))
async def langganan_modul_cbq(client, query: CallbackQuery):
    text = """<blockquote>💰 Modul Langganan

Paket yang tersedia:
• 1 Bulan: Rp25.000,-
• 3 Bulan: Rp60.000,-

Hubungi admin untuk informasi lebih lanjut.
</blockquote>"""
    admin_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Hubungi Admin", url=f"http://t.me/{OWNER_NAME}")],
            [InlineKeyboardButton("🔙 Kembali ke Menu Bot", callback_data="menu")]
        ]
    )
    await query.edit_message_text(text=text, reply_markup=admin_keyboard)
