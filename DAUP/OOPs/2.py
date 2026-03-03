class computer:
    
    brand = "Telusko"  #class Variable
    def __init__(self,cpu,ram,ssd):
        print("init called")
        self.cpu = cpu #Instance Variable
        self.ram=ram
        self.ssd=ssd
    
    def config(self):
        print("Config:",self.cpu,self.ram,self.ssd)
        
    @classmethod
    def info(cls):  #Class Methods
        return cls.brand

com1 = computer("i5","16gb","512gb")
com2 = computer("i9","64GB","2TB")


com1.config()
com2.config()

print(computer.info())