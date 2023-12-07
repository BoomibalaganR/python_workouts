from model.entity.product import Product

class DiscountedProduct(Product):
    
    def __init__(self, id, name, price, quantity, percentage = 0):
        super().__init__(id, name, price, quantity)
        self.__discount_percent = float(percentage)
    

    def get_discount(self):
        return self.__discount_percent
    
    def get_price(self):   
        discount_amount = self._price *(self.__discount_percent/100) 
        return self._price - discount_amount

    def set_price(self, price):
        self._price = price  
        
    def to_dict(self):
        return {"_id": super().get_id(), "name": super().get_name(), 
                "price": super().get_price(), "quantity": super().get_quantity(),
                "discount": self.get_discount()}
        
   