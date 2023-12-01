from model.Db.Database import Database 
from model.entity.Topic import Topic

class Request:  
    
    #get list of topics only 
    @staticmethod
    def get_listOf_topics():
       topics = Database.DictOf_Topics.keys()
       return list(topics)
    
    #get all problem from particular topic,return Topic object
    @staticmethod
    def get_AllProblemByID(key): 
        return Database.DictOf_Topics.get(key)
    
         
         
         
        