import mysql.connector as condb

try:

	mydb = condb.connect(host="localhost",user="yuva",passwd="yuva",database="sys")

	mycursor = mydb.cursor()

	mycursor.execute("select * from mytest")

	result = mycursor.fetchone()

	for i in result:
		print(i)

except Exception as e:

    print(e)

finally:
	mydb.close()