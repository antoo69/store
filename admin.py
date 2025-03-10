import os
import sys
import json
import shutil
from datetime import datetime
from pyrogram import Client, filters
from config import OWNER_USERNAME

def is_admin(func):
    async def wrapper(client, message):
        if message.from_user.username == OWNER_USERNAME:
            await func(client, message)
        else:
            await message.reply_text("⚠️ This command is only for admin!")
    return wrapper

@is_admin
async def backup_db(client, message):
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{backup_dir}/shop_bot_{timestamp}.db"
    
    try:
        shutil.copy2(DB_PATH, backup_path)
        await message.reply_text(f"✅ Database backup created successfully!\nFile: {backup_path}")
    except Exception as e:
        await message.reply_text(f"❌ Backup failed: {str(e)}")

@is_admin
async def restore_db(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply_text("⚠️ Please reply to a database backup file!")
        return
    
    try:
        file = await message.reply_to_message.download()
        shutil.copy2(file, DB_PATH)
        os.remove(file)
        await message.reply_text("✅ Database restored successfully!")
    except Exception as e:
        await message.reply_text(f"❌ Restore failed: {str(e)}")

@is_admin
async def update_bot(client, message):
    try:
        os.system('git pull')
        await message.reply_text("✅ Bot updated successfully! Use /restart to apply changes.")
    except Exception as e:
        await message.reply_text(f"❌ Update failed: {str(e)}")

@is_admin
async def restart_bot(client, message):
    await message.reply_text("🔄 Restarting bot...")
    os.execl(sys.executable, sys.executable, *sys.argv)
