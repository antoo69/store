from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🛍 Produk", callback_data="produk")],
        [types.InlineKeyboardButton(text="📖 Cara Order", callback_data="cara_order")],
        [types.InlineKeyboardButton(text="💰 Harga", callback_data="harga")]
    ])

    text = "👋 Selamat datang di Store Bot!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order."
    await message.answer(text, reply_markup=keyboard)
