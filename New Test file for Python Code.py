class Device:
    def __init__(self,name):
        print("Init called for",name)
        self.name = name.upper()
    
    def show(self):
        print("Device:", self.name)


d1 = Device("laptop")
d2 = Device("mobile")

d1.show()
d2.show()
