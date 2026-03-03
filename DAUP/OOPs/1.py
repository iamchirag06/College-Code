class Dog:
    #class variable
    spieces ="canine"
    
    def __init__(self, name, age):
        self.name = name #instance variable
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.spieces)
print(dog1.name)  
print(dog2.name)

dog1.name="max"
print(dog1.name)

Dog.spieces="Feline"
print(dog1.spieces)
print(dog2.spieces)