import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
''')

conn.commit()

users = ["Ali", "Aigerim", "Bek", "Nura", "Timur"]

for user in users:
    cursor.execute("INSERT INTO users (name) VALUES (?)", (user,))

# movies = [
#     ("Inception", "Sci-Fi"),
#     ("Titanic", "Drama"),
#     ("Avengers", "Action"),
#     ("Joker", "Drama"),
#     ("Interstellar", "Sci-Fi")
# ]

# for movie in movies:
#     cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", movie)

# reviews = [
#     (1, 1, 9),
#     (1, 2, 8),
#     (2, 1, 10),
#     (2, 3, 7),
#     (3, 4, 9),
#     (3, 5, 8),
#     (4, 2, 6),
#     (4, 3, 7),
#     (5, 1, 10),
#     (5, 5, 9)
# ]

# for review in reviews:
#     cursor.execute(
#         "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
#         review
#     )

# conn.commit()

print("\nОтзывы:")
cursor.execute('''
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
''')

for row in cursor.fetchall():
    print(row)


print("\nВсе фильмы:")
cursor.execute('''
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
''')

for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT AVG(rating) FROM reviews')
print("\nСредняя оценка:", cursor.fetchone()[0])

cursor.execute('SELECT MAX(rating) FROM reviews')
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute('SELECT MIN(rating) FROM reviews')
print("Минимальная оценка:", cursor.fetchone()[0])

# Отзывы:
# ('Ali', 'Inception', 9)
# ('Ali', 'Titanic', 8)
# ('Aigerim', 'Inception', 10)
# ('Aigerim', 'Avengers', 7)
# ('Bek', 'Joker', 9)
# ('Bek', 'Interstellar', 8)
# ('Nura', 'Titanic', 6)
# ('Nura', 'Avengers', 7)
# ('Timur', 'Inception', 10)
# ('Timur', 'Interstellar', 9)
#
# Все фильмы:
# ('Inception', 9)
# ('Inception', 10)
# ('Inception', 10)
# ('Titanic', 6)
# ('Titanic', 8)
# ('Avengers', 7)
# ('Avengers', 7)
# ('Joker', 9)
# ('Interstellar', 8)
# ('Interstellar', 9)
#
# Средняя оценка: 8.3
# Максимальная оценка: 10
# Минимальная оценка: 6