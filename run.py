import asyncio
import logging
from bot import dp, bot
import start  # Pastikan handler `/start` dimuat

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Masukkan router dari start.py
dp.include_router(start.router)

async def main():
    logging.info("🚀 Bot sedang berjalan...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
