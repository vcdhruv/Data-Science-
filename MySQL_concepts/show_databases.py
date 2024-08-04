import mysql_configuration as mc

my_db = mc.connect_to_mysql()

mycursor = my_db.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)