import sqlite3 as sql

conn = sql.connect('user.db')
c = conn.cursor()

query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)'

c.execute(query)
print('Table user created')
conn.commit()

# c.execute('SELECT * FROM users')
# print(c.fetchall())