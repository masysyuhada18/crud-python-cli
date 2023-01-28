import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, addres) VALUES (%s, %s)"
val = ("Hada","Samarinda")

cursor.execute(sql,val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))