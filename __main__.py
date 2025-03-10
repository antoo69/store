import asyncio
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from database import init_db

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Inisialisasi bot
app = Client(
    "shop_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    try:
        # Inisialisasi database
        await init_db()
        
        # Register semua handlers
        register_handlers(app)
        
        # Start bot dengan metode bawaan Pyrogram
        logger.info("Bot is starting... ✅")
        app.run()  # Ini akan otomatis menjaga bot tetap berjalan

    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()  # Tidak perlu `asyncio.run(main())`, karena `app.run()` sudah cukup
