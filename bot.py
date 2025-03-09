from aiogram import Bot, Dispatcher
from config import TOKEN
 # Tambahkan ini

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)  # Masukkan router ke dalam dispatcher
