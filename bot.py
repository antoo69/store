from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN, parse_mode="HTML")  # Tambahkan parse_mode opsional
dp = Dispatcher()  # Dispatcher tanpa bot
