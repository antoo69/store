import sqlite3
import json

DB_NAME = "store.db"

def init_db():
    """Membuat database dan tabel jika belum ada."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            price TEXT NOT NULL,
                            description TEXT NOT NULL)''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def add_products_from_json(json_file):
    """Menambahkan produk dari file JSON ke database."""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            products = json.load(file)

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        for product in products:
            cursor.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)",
                           (product["name"], product["price"], product["description"]))
        conn.commit()
    except (sqlite3.Error, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def get_products():
    """Mengambil semua produk (id & name) dari database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM products")
        products = cursor.fetchall()
        return [dict(product) for product in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

def get_product_by_id(product_id):
    """Mengambil detail produk berdasarkan ID."""
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, description FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        return dict(product) if product else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

# Inisialisasi database saat file diimpor
init_db()
