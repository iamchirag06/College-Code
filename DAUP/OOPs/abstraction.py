#abstraction

from abc import ABC, abstractmethod

class PaymentGateway(ABC):  #Abstract method
    @abstractmethod
    def pay(self):
        pass
    
class TeluskoPay(PaymentGateway):
    def pay(self):
        print("Pay Using TeluskoPay")
        
class Razorpay(PaymentGateway):
    def pay(self):
        print("Pay Using Razorpay")
        
class Purchase:
    
    def __init__(self,gateway):
        self.gateway=gateway
        
    def checkout(self):
        print("Checking Out..")
        
        self.gateway.pay()

gateway1 = Razorpay()
gateway2 = TeluskoPay()
purchase = Purchase(gateway2)

purchase.checkout()