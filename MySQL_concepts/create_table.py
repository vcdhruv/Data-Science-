import mysql_configuration as mc

mydb = mc.connect_to_mysql()

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT , c2 VARCHAR(50) , c3 FLOAT , c4 INT , c5 VARCHAR(30))")
mydb.close()