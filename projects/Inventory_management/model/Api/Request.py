from model.Database.dbConnection import InventoryDB


def add_product(product):
    if InventoryDB.create(product): 
       return "200"                     # return success code
          

def get_all_product():
    return InventoryDB.read()                           # return list of product dictionary
    

def get_product_byID(product_id):                       # get product using id
    product = InventoryDB.read({"_id": product_id})     # read from database
    if len(product) == 0:                               # if product is not found
        return "404"                                    # return not found code 
    
    return product[0]                                   # otherwise return product


def get_product_by_name(product_name):                  # get product using name
    product = InventoryDB.read({"name": product_name})  # read from database
   
    if len(product) == 0:                               # if product is not found
        return "404"                                    # return not found code 
  
    return product[0]                                   # otherwise return product


def update_product(product_id, product_dict):           # update product detail using id  
    updateStatus = InventoryDB.update(product_id,        
                                      product_dict)     # update product into DB
    if updateStatus.modified_count == 1:                # check if product is updated, 
        return "200"                                    # return success code, otherwise
    return "404"                                        # return not found code


def delete_product(product_id):                         # delete product detail using id
    deleteStatus = InventoryDB.delete(product_id)       # delete product from DB
    
    if deleteStatus.deleted_count == 1:                 # check if product is deleted
        return "200"                                    # return success code, otherwise
    return "404"                                        # return not found code