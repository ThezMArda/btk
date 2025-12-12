import sqlite3
conn =sqlite3.connect("veritabani.db")
cursor=conn.cursor()
while(True):
    ilk_isim=input("isminizi girin")
    son_isim=input("soyisminizi girin")
    mail=input("mailinizi girin")
    cursor.execute(f"INSERT INTO 'customers' VALUES('{ilk_isim}','{son_isim}','{mail}')")

    cikis=input("çıkmak için q basin")
    if cikis == "q":
        break
cursor.execute("SELECT rowid,* FROM customers  ")
items=cursor.fetchall



conn.commit()
conn.close()
