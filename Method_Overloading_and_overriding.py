class Add:

    def sum(self,a=None,b=None,c=None): #there is no method overloading available in python like other programming languages, instead we can do our logic for overloading 
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

a1 = Add()
print(a1.sum(1,5))

class A():

    def show(self):
        print("in A")

class B(A):

    def show(self):  #it will check for show method in B if not available then it will check in the parent class A
        print("inside B")

b1 = B()
b1.show()
