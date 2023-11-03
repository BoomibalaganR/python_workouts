from abstract_Class.AbstractPayment import AbstractPayment

class Paytm(AbstractPayment):
   
    def __init__(self, amount):
       self.amount  = amount 
       
    def payAmount(self):
        print("{} is paid via Paytm..".format(self.amount))
    