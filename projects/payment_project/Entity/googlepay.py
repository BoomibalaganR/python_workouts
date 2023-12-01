from abstract_Class.AbstractPayment import AbstractPayment 

#entity
class GooglePay(AbstractPayment): 
   
    def __init__(self,amount): 
        self.amount = amount
    
    def payAmount(self):
       print("{} is paid via googlePay..".format(self.amount))