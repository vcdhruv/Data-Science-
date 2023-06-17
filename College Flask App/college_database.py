import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)

print(my_db)
mycursor = my_db.cursor()
mycursor.execute("CREATE DATABASE if not exists College_Students")
my_db.close()