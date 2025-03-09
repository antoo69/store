import asyncio
import logging
from bot import dp, bot
import handlers  # Pastikan ini ada
from start import router as start_router  # Tambahkan ini!

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("🚀 Bot sedang berjalan...")

    # Tambahkan router dari start.py
    dp.include_router(start_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
