from model.entity.product import Product 
from view import home_ui, product_ui, product_input, product_search, sales_report_ui

from api import Request    


def add():
    product = product_input.form()
    response =  Request.add_product(product) 
    print(response["message"]) 
    
    input("please enter to continue...")
       
       
def update(): 
    
    while(True):                                    # get product name
        name = input("Enter product Name: ")  
        if name.isalpha():  
            break 
        print("invalid literal...\n") 
    
    while(True):   
        try:  
            quantity = int(input("Enter product quantity: ")) # get product quantity  
            break
        except:
            print("invalid literal")
   
    response = Request.update_product(name, int(quantity)) 
    print(response["message"]) 
    input("\nplease enter to continue...") 


def search():
    product_name = product_search.form()                # get product name for search 
    response = Request.get_product_by_name(product_name, {"_id": 0}) # request for product using product name
    
    if response["status_code"] == 200:
        product_ui.display(response)                         # display product
    else:
        print(response["message"])
    input("please enter to continue...") 


def delete():
     
    while(True):                                        # get product name
        name = input("\nEnter product Name: ")  
        if  name.isalpha():   
            break
        print("invalid literal...\n") 
                 
    response = Request.delete_product(name)
    print(response["message"])
            
    input("please Enter to continue...")


def display(): 
    
    response = Request.get_all_product()       # request for get all product detail
    product_ui.display(response)             # display product
    input("please enter to continue...")  


def place_order(): 
    
    while(True):                                    # get product name
        customer_name = input("Enter customer Name: ")  
        if customer_name.isalpha():  
            break 
        print("invalid literal...\n") 
    
    while(True):                                    # get product name
        product_name = input("Enter product Name: ")  
        if product_name.isalpha():  
            break 
        print("invalid literal...\n") 
    
    while(True):    
        try: 
            quantity = int(input("Enter product quantity: ")) # get product quantity
            
            if int(quantity) <= 0:
                print("please enter Non negative quantity...") 
            else:
                break
        except:
            print("invalid literal... \n") 
    
    response = Request.create_order(customer_name.title(), product_name, quantity) 
      
    print(response)
    input("please enter to continue...")



def genarate_sales_report():
    
    response = Request.get_sales_report()
    sales_report_ui.display(response)
    
    input("please enter to continue...")


def recommend_product():
    while(True):                                    # get customer name
        customer_name = input("Enter customer Name: ")  
        if customer_name.isalpha():  
            break 
        print("invalid literal...\n")  
        
    while(True):                                    # get number of product
        num_recommend = input("Enter num recommendation : ")  
        if num_recommend.isnumeric():  
            break 
        print("invalid literal...\n") 
    
    #print(customer_name, num_recommend)
    response = Request.get_recommend_product(customer_name, int(num_recommend) ) 
    
    if response["status_code"] == 200:
       for document in response["data"]:
           print(document["product_name"])
       
    else:
        print(response["message"])
    
    input("please enter to continue...")

