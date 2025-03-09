from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))  # Perbaikan di sini
dp = Dispatcher()  # Dispatcher tanpa bot
