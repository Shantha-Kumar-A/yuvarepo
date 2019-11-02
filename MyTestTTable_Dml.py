import MySQL_DB as db
import MyTestTablePojo as tab 

try:

	connopen = db.OpenConn(host="localhost",user="yuva",passwd="yuva",db="sys")

	cursor = connopen.cursor()

	obj = tab.mytest(id=1,name='')

	

	query = obj.fetchdata()

	print(query)

	cursor.execute(query) #fetch

	resfetch = cursor.fetchone()

	print(resfetch)

	for i in resfetch:
		if i == "yuva":
			obj.name = "yuvaraj"
		else:
			obj.name = "yuva"

	updatequery = obj.updatedata()

	print(updatequery)

	cursor.execute(updatequery)

	obj.name = "Ram"

	deletequery = obj.deletedata();

	print(deletequery)

	cursor.execute(deletequery)

	insertquery = obj.insertdata()

	print(insertquery)

	cursor.execute(insertquery)

except Exception as e:

	connopen.rollback()

	print(e)

finally:

	if connopen.is_connected():
		connopen.commit()
	
	db.CloseConn


