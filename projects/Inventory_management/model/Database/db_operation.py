from model.Database.dbConnection import DB

   
class Database: 
    
    @staticmethod
    def create( collection_name, data):                                     # create new product 
       
        collection = DB.get_connection(collection_name)          # get connection to product collection
     
        try:
            id = collection.insert_one(data)  # insert product dictionary to db 
        except :  
            return None
        return  id.inserted_id
    

    @staticmethod
    def update( collection_name, id , new_value):            # update product details
        product_coll = DB.get_connection(collection_name)         # get connection to product collection
        
        return product_coll.update_one(id, {"$set": new_value}) 
         
     
    @staticmethod
    def read( collection_name, query = {}, project = {"_id": 0}):                                      # read products
        product_coll = DB.get_connection(collection_name)         # get connection to product collection
        
        return list(product_coll.find(query, project))                  # return list of product dictionary


    @staticmethod
    def delete( collection_name, query):                                         # delete product
        product_coll = DB.get_connection(collection_name)         # get connection to product collection
        return product_coll.delete_one(query).deleted_count        # return deleted product status
        

    @staticmethod
    def aggregate(collection_name, pipeline):
        order_coll = DB.get_connection(collection_name) 
        
        return list(order_coll.aggregate(pipeline))
        




    
    