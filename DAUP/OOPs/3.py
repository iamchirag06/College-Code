class A:
    
    def __init__(self):
        print("init A called")
    def f1(self):
        print("f1 works")
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print("init B called")
    def f2(self):
        self.f1()
        print("f2 works")    
           
obj1 = B()
obj1.f2()
