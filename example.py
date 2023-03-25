import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT*FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

new_rows = [('Cats', 'Cats City', '2088.10.15'),
            ('Lynx', 'Lynx City', '2088.11.15')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()
