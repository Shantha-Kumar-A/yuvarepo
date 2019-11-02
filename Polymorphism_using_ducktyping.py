class idle():

    def execute(self):
        print("compiling")
        print("running")

class myeditor():

    def execute(self):
        print("spell checking")
        print("conventional checking")
        print("compiling")
        print("running")

class computer():

    def code(self,ide):
        ide.execute() #duck typing -- there should be the method execute() in the called class object


ideo = idle()
ideown = myeditor()

comp1 = computer()

comp1.code(ideown)
