from abc import ABC, abstractmethod

#AbstractClass
class AbstractPayment(ABC):
    
    @abstractmethod
    def payAmount(self): 
        pass
    