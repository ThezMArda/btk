import sqlite3
conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO customers VALUES('mary','brown','mail@gmail.com')")
conn.commit()
conn.close
