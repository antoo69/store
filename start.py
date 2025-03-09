from aiogram import types, Router
from bot import dp

router = Router()

@router.message(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🛍 Produk", "📖 Cara Order", "💰 Harga")

    text = "👋 Selamat datang di Store Bot!\n\nSilakan pilih menu di bawah ini untuk melihat produk dan cara order."
    await message.answer(text, reply_markup=keyboard)

dp.include_router(router)  # Tambahkan router ke dispatcher
