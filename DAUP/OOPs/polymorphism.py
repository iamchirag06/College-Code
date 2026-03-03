#Polymorphism
# One thing in different forms

#Duck typing
class Laptop:   #Duck
    def build(self):
        print("Laptop Builds")

class Desktop(): #Crow
    def build(self):
        print("Desktop Builds")

class Alien:
    def code(self,machine:Laptop):
        print("Alien Building")
        machine.build()
        
asus_rog = Laptop()
beast = Desktop()

navin = Alien()
# navin.code(asus_rog)
navin.code(beast)



