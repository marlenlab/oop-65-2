import sqlite3

# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()

# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")')
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )

    connect.commit()
    print('Пользователь добавлен!!')

create_user("Марлен", 13, "Горы!!")
create_user("Кайрат", 13, "Горы!!")
create_user("Данияр", 13, "Горы!!")

def read_users():
    cursor.execute('SELECT name, hobby FROM users')
    user = cursor.fetchmany(3)
    print(f"all users\n {user}")

# read_users()

def update_user(new_name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (new_name, rowid)
    )
    connect.commit()
    print("User updated!!")

# update_user("John", 3)

# read_users()

def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print('Пользователь удален!!')

# delete_user(2)