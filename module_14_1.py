import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(11):
 #   username = 'User' + str(i)
  #  email = 'example' + str(i) + '@gmail.com'
   # age = 10 * i
    #balance = 1000
    #cursor.execute("INSERT INTO USERS (username, email, age, balance) values (?,?,?,?)",
     #              (username, email, age, balance))
#for i in range(11):
    #if i % 2 == 0:
        #cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
#for i in range(11):
    #if i % 3 == 0:
        #cursor. execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
_print = cursor.fetchall()
for i in _print:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')
connection.commit()
connection.close()