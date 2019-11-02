import mysql.connector as condb

def OpenConn(host,user,passwd,db):

	 mydb = condb.connect(host=host,user=user,passwd=passwd,database=db)

	 return mydb

def CloseConn():
	mydb.close()