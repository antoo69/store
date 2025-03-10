import asyncio
import logging
import sqlite3
from pyrogram import Client, filters, enums
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from database import init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
app = Client(
    "shop_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    try:
        # Initialize database
        await init_db()
        
        # Register all handlers
        register_handlers(app)
        
        # Start the bot
        await app.start()
        logger.info("Bot started successfully!")
        
        # Keep the bot running
        await app.idle()
        
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
