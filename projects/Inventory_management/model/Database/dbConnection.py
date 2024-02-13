import pymongo


class DB: 
    
    __myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
    __database = "ecommerce" 
    
    
    @classmethod
    def get_connection(cls, collection): 
        db = cls.__myclient[cls.__database] 
        return db[collection]  

    
    