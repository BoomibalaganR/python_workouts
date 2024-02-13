from services.service import *
from view import home_ui

while(True): 
    home_ui.display()    # display menu
    
    try:
        choice = int(input("Enter your choice: "))  # get choice
    except:
        print("enter valid literals")
        continue
    
    
    if choice == 1:                                     # add product
        add()
       
    elif choice == 2:                                   # update product     
       update()
    
    elif choice == 3:                                       # search product 
        search()
        
    elif choice == 4:                                       # remove product 
       delete()
          
    elif choice == 5: # display inventory 
        display()
       
    elif choice == 6:                                       # place order
       place_order()
     
    elif choice == 7:                                       # sale report
       genarate_sales_report()
    
    elif choice == 8:                                       # recommend_product
       recommend_product()
    
    elif choice == 9:                                       # exit program
        print("\n\t\t<<<Thank You>>>")
        break 
    
    else:
        print("please Enter valid choice (1-5).....") 
        

