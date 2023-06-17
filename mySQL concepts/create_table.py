import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT , c2 VARCHAR(50) , c3 FLOAT , c4 INT , c5 VARCHAR(30))")
mydb.close()