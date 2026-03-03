class abc:
    
    def __init__(self):
        print("init called")
        
    def show(self):
        print("in show")
        
obj1 = abc()
obj1.show()

obj2 = abc()
obj2.show()