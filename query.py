import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("select * from test1.test_table")
mycursor.execute("select c1 , c5 from test1.test_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()