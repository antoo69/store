import asyncio
import logging
from bot import dp, bot

# Konfigurasi logging agar ada output di VPS
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("🚀 Bot sedang berjalan...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
