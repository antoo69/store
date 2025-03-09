import asyncio
import logging
from bot import app  # Ambil instance bot yang sudah dibuat
import start  # Pastikan handler dari start.py dimuat

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("🚀 Bot sedang berjalan...")
    await app.start()
    logging.info("✅ Bot telah aktif")
    await asyncio.Event().wait()  # Menjaga bot tetap berjalan

if __name__ == "__main__":
    asyncio.run(main())
