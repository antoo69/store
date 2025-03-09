import asyncio
import logging
from bot import app  # Menggunakan app dari bot.py

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("🚀 Bot sedang berjalan...")
    await app.start()
    
    # Debugging: pastikan bot aktif
    me = await app.get_me()
    logging.info(f"✅ Bot telah aktif sebagai @{me.username}")

    await asyncio.Event().wait()  # Menjaga bot tetap berjalan

if __name__ == "__main__":
    asyncio.run(main())
