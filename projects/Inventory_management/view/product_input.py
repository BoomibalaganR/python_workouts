from model.Database.dbConnection import InventoryDB 
from entity.product import Product 
from entity.discount_product import DiscountedProduct  


def form():
    while(True):    # get product id 
        
        id = input("Enter product id: ")
        
        if not id.isnumeric(): 
            print("invalid literal...\n") 
            continue
        
        if InventoryDB.is_idExits(int(id)): 
            break  
        print("id already exits....\n") 
        
    
    while(True):                                   # get product name
        name = input("Enter product Name: ")  
        if name.isalpha(): 
            break
        print("invalid literal...\n") 
            
        
    while(True): 
        price = input("Enter product price: ")      # get product price
        if price.isnumeric():
            break
        print("invalid literal... \n") 
         
        
    while(True):    
        quantity = input("Enter product quantity: ") # get product quantity
        if quantity.isnumeric():
            break
        print("invalid literal... \n") 
         
         
    while(True):                                       # get discount if exit
        discount = input("Enter discount percent ( if exit otherwise press 0 )")
        if discount.isnumeric():
            break
        print("invalid literal... \n")   
    
    
    if discount == '0':
        return Product(id, name, price, quantity)
    return  DiscountedProduct(id, name, price, quantity, discount)
  