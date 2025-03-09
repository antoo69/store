from aiogram import Bot, Dispatcher
from config import TOKEN
from database import init_db, add_products_from_json

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

init_db()
add_products_from_json("products.json")
