class Product: 
  
    def __init__(self, id, name, price, quantity): 
    
        self.__id = int(id)
        self.__name = name 
        self._price = float(price) 
        self.__quantity = int(quantity) 
    
    
    def get_id(self):
        return self.__id  
    
    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name
    
    def get_price(self): 
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    
    def get_quantity(self):
        return self.__quantity 
    
    def set_quantity(self, quantity):
        self.__quantity = quantity 
        
    def to_dict(self):
        return dict(_id= self.__id, name = self.__name, price=self._price,
                    quantity= self.__quantity)