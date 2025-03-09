import sqlite3
import json

def init_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        price TEXT,
                        description TEXT)''')
    conn.commit()
    conn.close()

def add_products_from_json(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        products = json.load(file)
    
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    for product in products:
        cursor.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)",
                       (product["name"], product["price"], product["description"]))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, description FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product
