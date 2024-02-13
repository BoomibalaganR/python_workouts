from model.entity.product import Product 

from api import Request


def form():
  
    """
    while(True):    # get product id 
        
        id = input("Enter product id: ")
        
        if not id.isnumeric(): 
            print("invalid literal...\n") 
            continue
        
        if InventoryDB.is_idExits(int(id)): 
            break  
        print("id already exits....\n") 
    """     
    
    while(True):                                   # get product name
        name = input("\nEnter product Name: ")  
        if not name.isalpha():  
            print("invalid literal...\n") 
            continue  
        response = Request.is_nameExit(name)
        if  response["status_code"] == 404:
            break 
        print(response["message"])
       
            
        
    while(True): 
        price = input("Enter product price: ")      # get product price
        if price.isnumeric():
            break
        print("invalid literal... \n") 
         
        
    while(True):    
        try: 
            quantity = int(input("Enter product quantity: ")) # get product quantity
            
            if int(quantity) < 0:
                print("please enter Non negative quantity...") 
            else:
                break
        except:
            print("invalid literal... \n") 
    
    return Product( name, price, quantity)
    
  