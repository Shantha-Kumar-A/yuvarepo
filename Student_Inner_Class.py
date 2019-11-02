class student:

    school = "SVM"

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        #self.lap = self.laptop("HP","i3",8,"1TB") #an object of the inner class can be created inside the outer class

    def show(self):
        print(self.name,self.rollno)
        #self.lap.show()

    class laptop:  #inner class

        def __init__(self,brand,cpu,ram,storage):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            self.storage = storage

        def show(self):
            print(self.brand,self.cpu,self.ram,self.storage)

s1 = student("Yuvi",105)
s2 = student("Hari",109)

lap = s1.laptop("HP","i3",8,"1TB")   #an object of the inner class can be created outside the outer class

s1.show()
lap.show()
