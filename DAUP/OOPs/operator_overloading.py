class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def __str__(self):
        return f'{self.name} : {self.balance}'
    
    def __add__(self,other):
        return Account('combined',self.balance + other.balance)
    def __gt__(self, other):
        return self.balance > other.balance
    
user1 = Account("Chirag",4000)
user2 = Account("Kashish",2000)

combined = user1 + user2
print(user1)     
print(user2)
print(combined)

if user1 > user2:
    print("Chirag Pay the Bill")
else:
    print("Kashish pay the bill")