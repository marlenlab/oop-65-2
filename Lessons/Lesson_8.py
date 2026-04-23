import sqlite3

connection = sqlite3.connect('grade.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR(30) NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

def create_user(name, age):
    cursor.execute(
        'INSERT INTO users (name, age) VALUES (?, ?)',
        (name, age)
    )
    connection.commit()
    print('User added')

def create_grade(grade, subject, user_id):
    cursor.execute(
        'INSERT INTO grades (grade, subject, user_id) VALUES (?, ?, ?)',
        (grade, subject, user_id)
    )
    connection.commit()
    print('Grade added')

create_user('Ardager', 27)
create_user('Oleg', 21)
create_user('Misha', 23)
create_grade('5', 'Физра',1)
create_grade('3', 'Физра',1)
create_grade('3', 'Физра',1)


