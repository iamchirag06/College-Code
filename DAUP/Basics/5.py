class Circle:
    def __init__(self,r):
        self.r = r
        
    def area(self):
        a = 3.14*self.r**2
        return a

ins = Circle(5) 
print("Area of Circle:",ins.area())