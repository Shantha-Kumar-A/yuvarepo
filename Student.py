class student:

    school = "SVM"

    def __init__(self,m1,m2,m3):         #instance method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod                      #class method which is defined with a special decorator as @classmethod
    def Getschool(cls):               #cls keyword should not be changed and it should be used as such.
        return cls.school

    @staticmethod                     #static method which is defined with a special decorator as @staticmethod
    def info():                       #Doesn't require any arguments like instance(self) or class(cls) methods
        print("This is student class 123")

s1 = student(50,70,90)
s2 = student(60,70,80)

print(s1.avg())
print(student.Getschool())

student.info()
