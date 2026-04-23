import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

conn.commit()

def create_product(name, price, quantity):
    cursor.execute('''
        INSERT INTO products (name, price, quantity)
        VALUES (?, ?, ?)
    ''', (name, price, quantity))
    conn.commit()

def read_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)


def update_product(id, price):
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (price, id))
    conn.commit()


def delete_product(id):
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (id,))
    conn.commit()

create_product("Laptop", 1000, 5)
create_product("Phone", 500, 10)

print("До обновления:")
read_products()

update_product(1, 1200)

print("\nПосле обновления:")
read_products()

delete_product(2)

print("\nПосле удаления:")
read_products()

conn.close()
