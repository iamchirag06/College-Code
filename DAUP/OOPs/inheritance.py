#Inheritance
class A: #Parent Class
    def f1(self):
        print("f1 works")
    def f2(self):
        print("f2 works")
    def show(self):
        print("In A Show")
        
class B:  #Child Class
    def f3(self):
        print("f3 works")
    def f4(self):
        print("f4 works")
    def show(self):
        print("In B Show")    

class C(A,B): #Multiple Inheritance
    def f5(self):
        print("f5 works")
    # def show(self):
    #     print("In C Show")


obj1 = C()
B.show(obj1)