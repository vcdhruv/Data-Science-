import mysql_configuration as mc

mydb = mc.connect_to_mysql()

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(1,'vishmay',777.777,7,'dhruv')")
mycursor.execute("insert into test1.test_table values(1,'chetanbhai',777.777,7,'dhruv')")
mycursor.execute("insert into test1.test_table values(1,'meetaben',777.777,7,'dhruv')")
mycursor.execute("insert into test1.test_table values(1,'drashty',777.777,7,'dhruv')")
mycursor.execute("insert into test1.test_table values(1,'krish',777.777,7,'kothari')")
mycursor.execute("insert into test1.test_table values(1,'devansh',777.777,7,'jadav')")

mydb.commit()
mydb.close()