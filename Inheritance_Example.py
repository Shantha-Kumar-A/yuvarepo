class A():

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class A1():

    def feature1_1(self):
        print("feature 1.1 is working")

    def feature2_1(self):
        print("feature 2.1 is working")
        
class B(A): #single level inheritance

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

b1 = B()
b1.feature1()
b1.feature3()

class C(B): #multilevel inheritance

    def feature5(self):
        print("feature 5 is working")

c1 = C()

c1.feature4()

class D(A1,A): #multiple inheritance

    def feature6(self):
        print("feature 6 is working")

d1 = D()

d1.feature2_1()
