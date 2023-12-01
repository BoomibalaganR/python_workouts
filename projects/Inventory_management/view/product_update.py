from model.Database.dbConnection import InventoryDB
import re 


def form():

    update_dict = dict()     
    while(True): 
            print(" if you want to update column enter one by one  (key: value), otherwise enter exit. ex name:wheat ")

            while(True):  
                
                column_value = input()      # get input coulum name and value
                if column_value == 'exit':
                    return update_dict      # return updated product dictionary
                               
                if len(column_value)==0 or re.match( "[a-z A-Z]+:[a-z A-Z 0-9]+",column_value) is None:
                    print("Enter valid input...")
                    continue  
                
                ls = column_value.split(":") # split into column_name and value
                key = ls[0]
                value = ls[1] 
                
                update_dict[key] = value     # add new value into dictionary
                 
        