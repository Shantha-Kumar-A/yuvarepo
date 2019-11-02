class mytest:
    tablename = "mytest"
    pk = "id"
    column1 = "name"

    def __init__(self,id,name):

        self.id = id

        self.name = name

    def insertdata(self):
	    
	    prepstmt = "insert into "+str(mytest.tablename)+" values ("+"null"+","+"'"+str(self.name)+"'"+")"
	    
	    print(prepstmt)
	    
	    return prepstmt

    def deletedata(self):
	    
	    prepstmt = "delete from "+str(mytest.tablename)+" where "+str(mytest.column1)+" = "+"'"+str(self.name)+"'"
	    
	    return prepstmt

    def updatedata(self):
	    
	    prepstmt = "update "+str(mytest.tablename)+" set "+str(mytest.column1)+" ="+"'"+str(self.name)+"'"+" where "+str(mytest.pk)+" = "+str(self.id)
	    
	    return prepstmt

    def fetchdata(self):

    	prepstmt = "select * from "+str(mytest.tablename)+" where "+str(mytest.pk)+" = "+str(self.id)

    	return prepstmt
