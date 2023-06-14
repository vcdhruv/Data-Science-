import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mydb.close()