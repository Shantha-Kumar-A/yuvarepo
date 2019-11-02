class Employee:

    comp = "3i Infotech"  #Static or class variables
    
    def __init__(self):
        self.name = "Yuvaraj" #Instance or object variables
        self.age  = 25

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


emp1 = Employee()
emp2 = Employee()

emp2.name = "Mohanraj"
emp2.age = 25

Employee.comp = "Google"

if emp1.compare(emp2):
    print("They both are same")
else:
    print("They are different")

print(emp1.name+" is",emp1.age,"from "+emp1.comp)
print(emp2.name+" is",emp2.age,"from "+emp2.comp)
