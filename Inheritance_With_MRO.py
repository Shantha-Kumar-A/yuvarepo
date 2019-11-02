class A():

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A")

class B():

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature 1-B")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feature4(self):
        print("Feature 4 is called")

    def featsuper(self):
        super().feature1()   #calling a method of super class that is called first object of the class(A)
                             #MRO - Method resolution order, incase of multiple inheritance the class which is extended first that is A would be used for super method implementation

a1 = C()
a1.featsuper()
