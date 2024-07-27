import sqlite3

# Создаем подключение к базе данных (или создаем ее, если она не существует)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создаем таблицу countries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

# Вставляем данные в таблицу countries
cursor.executemany('''
    INSERT INTO countries (title) VALUES (?)
''', [('Kyrgyzstan',), ('Germany',), ('China',)])

# Создаем таблицу cities
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

# Вставляем данные в таблицу cities
cursor.executemany('''
    INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)
''', [
    ('Bishkek', 127.0, 1),
    ('Osh', 182.0, 1),
    ('Berlin', 891.8, 2),
    ('Munich', 310.7, 2),
    ('Beijing', 16411.0, 3),
    ('Shanghai', 6340.5, 3),
    ('Guangzhou', 7434.4, 3)
])

# Создаем таблицу students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

# Вставляем данные в таблицу students
cursor.executemany('''
    INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
''', [
    ('Alex', 'Johnson', 1),
    ('Mira', 'Lee', 1),
    ('Ivan', 'Petrov', 2),
    ('Olga', 'Ivanova', 2),
    ('Hans', 'Schmidt', 3),
    ('Anna', 'Müller', 3),
    ('Karl', 'Heinz', 4),
    ('Ingrid', 'Schneider', 4),
    ('Wei', 'Chen', 5),
    ('Li', 'Wang', 5),
    ('Xiao', 'Liu', 6),
    ('Hao', 'Zhang', 6),
    ('Mei', 'Huang', 7),
    ('Yan', 'Lin', 7),
    ('Qing', 'Xu', 7)
])

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("Database and tables created successfully.")
