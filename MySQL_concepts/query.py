import mysql_configuration as mc

mydb = mc.connect_to_mysql()

print(mydb)
mycursor = mydb.cursor()
print("all data")
mycursor.execute("select * from test1.test_table")
for i in mycursor.fetchall():
    print(i)

print("\nfirst and last column")
mycursor.execute("select c1 , c5 from test1.test_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()