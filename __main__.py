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
        
        # Start bot
        await app.start()
        logger.info("Bot started successfully! ✅")
        
        # Menjaga bot tetap berjalan
        await asyncio.Event().wait()

    except Exception as e:
        logger.error(f"Error occurred: {e}")

    finally:
        logger.info("Shutting down bot...")
        await app.stop()
        logger.info("Bot stopped.")

# Menjalankan bot dengan benar
if __name__ == "__main__":
    app.run()  # ✅ Ini sudah cukup, tanpa perlu asyncio.run()
