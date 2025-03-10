import asyncio
import logging
from bot import app
import start

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def main():
    try:
        logging.info("🚀 Starting bot...")
        await app.start()
        logging.info("✅ Bot is active")
        await asyncio.Event().wait()  # Keep the bot running
    except Exception as e:
        logging.error(f"❌ Error occurred: {str(e)}")
        raise e

if __name__ == "__main__":
    asyncio.run(main())
