from aiogram import Bot, Dispatcher
from config import TOKEN
from database import init_db

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

init_db()
