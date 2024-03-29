import pymongo 


class StudentDB: 
    
    __myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
    __database = "student_grades"
    __collection = "grades" 
    
    @classmethod
    def get_connection(cls): 
        db = cls.__myclient[cls.__database] 
        return db[cls.__collection]   
    
    
    
    @staticmethod
    def create(student_dict):                # create 
        print("student dic", student_dict)
        studentCollection = StudentDB.get_connection() 
        
        try:
            studentCollection.insert_one(student_dict) 
        except:
            return False 
        return True 
        
    
    
    @staticmethod                               # update 
    def update(query={}, newValue={}):
        student_collection = StudentDB.get_connection()
        return student_collection.update_one(query, {"$set": newValue})
    
    
    @staticmethod
    def read(query = {}, option = {}):            # read
        student_collection = StudentDB.get_connection() 
        return list(student_collection.find(query, option))
    
    def read_one(query = {},option = {}):
        student_collection = StudentDB.get_connection()
        return student_collection.find_one(query, option) 
        
    
    def aggregate(pipeline):
        student_collection = StudentDB.get_connection()
        return student_collection.aggregate(pipeline)