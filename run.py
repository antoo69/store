import asyncio
import logging
from pyrogram import Client
from config import *
app = Client("store_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("🚀 Bot sedang berjalan...")
    
    await app.start()
    logging.info("✅ Bot telah aktif")
    await asyncio.Event().wait()  # Menjaga bot tetap berjalan

if __name__ == "__main__":
    asyncio.run(main())
