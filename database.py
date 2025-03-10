import sqlite3
import aiosqlite
import json
from typing import Dict, List
from pathlib import Path

DB_PATH = "shop_bot.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS catalog (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS cart (
                user_id INTEGER,
                item_id TEXT,
                quantity INTEGER,
                FOREIGN KEY (item_id) REFERENCES catalog (id)
            )
        ''')
        await db.commit()

async def get_catalog() -> List[Dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute('SELECT * FROM catalog')
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
