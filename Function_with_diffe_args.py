def Add(a,b):
    c = a + b
    print(c)

Add(6,3)

def person(name,age=18):  #default value of 18 will be taken, if the arguments comes as null in the run time
    print(name)
    print(age)

#person(25,'Yuvaraj') #here the position of the parameters has been given wrongly and operation will also become wrong.
#To overcome the above problem, we can pass the arguments using its name
person(age=25,name='Yuvaraj')

def sum(a,*b): #* indicates that this parameter can have multiple values
    c = a
    for i in b:
        c = c + i
    print(c)

sum(1,2,3,4)
