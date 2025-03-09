from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
    keyboard = types.ReplyKeyboardMarkup(
         keyboard=[
             [types.KeyboardButton(text="🛍 Produk")],
             [types.KeyboardButton(text="📖 Cara Order")],
             [types.KeyboardButton(text="💰 Harga")]
         ],
         resize_keyboard=True
     )
 
     text = "👋 Selamat datang di Store Bot!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order."
     await message.answer(text, reply_markup=keyboard)
