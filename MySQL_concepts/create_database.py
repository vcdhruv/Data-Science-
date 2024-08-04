import mysql_configuration as mc

mydb = mc.connect_to_mysql()

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mydb.close()