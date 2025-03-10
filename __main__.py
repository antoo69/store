import asyncio
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from database import init_db

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Inisialisasi bot
app = Client("shop_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await init_db()  # Inisialisasi database
    register_handlers(app)  # 🔥 Mendaftarkan semua handler
    await app.start()  # 🔥 Menjalankan bot
    logger.info("Bot started successfully! ✅")
    await asyncio.Event().wait()  # Menjaga bot tetap berjalan

if __name__ == "__main__":
    asyncio.run(main())
