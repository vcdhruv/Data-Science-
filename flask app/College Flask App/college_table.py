import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists College_Students.student_details(student_name VARCHAR(50) , roll_no INT , SPI FLOAT , semester INT)")
mydb.close()