class Computer: ##Class definition
    
    def __init__(self,cpu,ram): #default method called as init will accept the variables and store in the object
        self.cpu = cpu
        self.ram = ram
        
    def config(self): ##Method definition
        print("Config is",self.cpu,self.ram)

com1 = Computer("i3",4) ##Object1 creation
com2 = Computer("Ryzen",8) ##Object2 creation

com1.config() ##Calling the method using object1
com2.config() ##Calling the method using object2
