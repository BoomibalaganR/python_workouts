from entity.discount_product import DiscountedProduct   
from entity.product import Product 
from view import home_ui,inventory_ui,product_ui,product_input,product_search,product_update
from model.Database.dbConnection import InventoryDB
 
from model.Api import Request    


while(True): 
    home_ui.display()    # display menu
    
    try:
        choice = int(input("Enter your choice: "))  # get choice
    except:
        print("enter valid literals")
        continue
    
    
    if choice == 1:                                     # add product
        product = product_input.form()
        if Request.add_product(product) == "200":       # raise request for add product
            print("successfully added...!!")        
        else:
            print("not sucessfully added...")
        input("please enter to continue...")
       
       
    elif choice == 2:                                   # update product 
        
        while(True):      
            product_id = input("Enter product id: ")    # get product id
        
            if product_id.isnumeric():  
                break
            print("invalid literal...\n") 
            

        product = Request.get_product_byID(int(product_id)) # request for get product detail by id
        product_ui.display(product)                         # display product
        
        if product != "404":                                # check if product is exit or not
            updated_product_dict = product_update.form()    # get update details
            
            if len(updated_product_dict) == 0:
                pass
            elif Request.update_product(int(product_id), updated_product_dict) == "200":# request for
                print("successfully updated...!!")                                      # update product
            else:
                print("not found...!!")
        input("please enter to continue...") 
        
          
    elif choice == 3:                                       # search product 
   
        product_name = product_search.form()                # get product name for search 
        product = Request.get_product_by_name(product_name) # request for product using product name
        product_ui.display(product)                         # display product
        
        input("please enter to continue...") 
       
       
    elif choice == 4:                                       # remove product 
        
        while(True):
            product_id = input("Enter product id: ")        # get product_name
            if product_id.isnumeric(): 
               break
            print("enter valid literal....")
        
        if Request.delete_product(int(product_id)) == '200': # request for delete product using id 
            print("successfully deleted....")
        else:
            print("given id not found...!!") 
            
        input("please Enter to continue...")
       
        
    elif choice == 5: # display inventory 
        listof_productDict = Request.get_all_product()       # request for get all product detail
        inventory_ui.display(listof_productDict)             # display product
        
        input("please enter to continue...")
       
        
    elif choice == 6:                                       # exit program
        print("\n\t\t<<<Thank You>>>")
        break 
    
    
    else:
        print("please Enter valid choice (1-5).....") 
        


