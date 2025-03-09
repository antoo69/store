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

start_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Produk", calback_data="product")
        ],
        [
            InlineKeyboardButton("Cara Order", callback_data="Order"),
            InlineKeyboardButton("Harga", callback_data="Harga")
        ],
        [
            InlineKeyboardButton("Owner", url="https://t.me/{OWNER_NAME}")
        ]
    ]
)

@app.on_message(filters.command("start"))
async def start_msg(client, message: Message):
    user = message.from_user.mention
    chat_type = message.chat.type

    if chat_type == CTYPE.PRIVATE:
        msg = f"<blockquote> Hi {user} !\n\nSaya bot store, Silahkan pilih produk yang ingin di beli </blockquote>"

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
