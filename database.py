import aiosqlite
from typing import Dict, List

DB_PATH = "shop_bot.db"

async def init_db():
    """Inisialisasi database dan buat tabel jika belum ada."""
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
    """Mengambil daftar katalog produk dari database."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute('SELECT * FROM catalog')
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

async def add_to_cart(user_id: int, item_id: str, quantity: int = 1):
    """Menambahkan produk ke dalam keranjang belanja."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT stock FROM catalog WHERE id = ?', (item_id,))
        row = await cursor.fetchone()
        
        if row and row[0] >= quantity:
            await db.execute('''
                INSERT INTO cart (user_id, item_id, quantity) 
                VALUES (?, ?, ?)
                ON CONFLICT(user_id, item_id) DO UPDATE SET quantity = quantity + ?
            ''', (user_id, item_id, quantity, quantity))
            await db.commit()
        else:
            raise ValueError("Stok tidak mencukupi atau item tidak ditemukan.")

async def get_cart(user_id: int) -> List[Dict]:
    """Mengambil daftar item yang ada dalam keranjang belanja pengguna."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute('''
            SELECT catalog.id, catalog.name, catalog.price, cart.quantity
            FROM cart
            JOIN catalog ON cart.item_id = catalog.id
            WHERE cart.user_id = ?
        ''', (user_id,))
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

async def remove_from_cart(user_id: int, item_id: str):
    """Menghapus item dari keranjang belanja."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('DELETE FROM cart WHERE user_id = ? AND item_id = ?', (user_id, item_id))
        await db.commit()

async def clear_cart(user_id: int):
    """Menghapus semua item dalam keranjang belanja pengguna."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('DELETE FROM cart WHERE user_id = ?', (user_id,))
        await db.commit()
