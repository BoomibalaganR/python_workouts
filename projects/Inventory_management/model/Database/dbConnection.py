import pymongo 


class InventoryDB: 
    
    __myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
    __database = "inventoryDB" 
    __collection = "products"
    

    @classmethod
    def get_connection(cls): 
        db = cls.__myclient[cls.__database] 
        return db[cls.__collection]  

    
    
    @staticmethod
    def create(product):                                     # create new product 
      
        product_coll = InventoryDB.get_connection()          # get connection to product collection
        try:
            id = product_coll.insert_one(product.to_dict())  # insert product dictionary to db
        except :  
            return False
        return True
    

    @staticmethod
    def update(product_id, updated_productDict):            # update product details
        product_coll = InventoryDB.get_connection()         # get connection to product collection
        
        return product_coll.update_one({"_id": product_id}, {"$set": updated_productDict}) 
         
     
    @staticmethod
    def read(id = {}):                                      # read products
        product_coll = InventoryDB.get_connection()         # get connection to product collection
        return list(product_coll.find(id))                  # return list of product dictionary


    @staticmethod
    def delete(id):                                         # delete product
        product_coll = InventoryDB.get_connection()         # get connection to product collection
        return product_coll.delete_one({"_id": id})         # return deleted product status
        

    @staticmethod 
    def is_idExits(id):                                     # check product id is exit or not
        
        product_coll = InventoryDB.get_connection()         # get connection to product collection
        product = product_coll.find_one({"_id": id})        # find product detail with given id
       
        return product is None                              # return if product exit or not
           
        


