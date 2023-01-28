import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_mainan")

print("Database berhasil dibuat!")