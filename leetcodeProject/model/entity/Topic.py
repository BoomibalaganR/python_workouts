from .Problem import Problem

class Topic: 
    
    __idCounter = 0
    
    def __init__(self,topicName):  
        Topic.__idCounter+=1 
        
        self.__topicID = Topic.__idCounter
        self.__topicName = topicName.title()
        self.__questionDict = {}
        
    def get_topicID(self):  
        return self.__topicID 
    
    def get_topicName(self): 
        return self.__topicName 
    
    def add_question(self,problem):
        self.__questionDict[problem.get_ID()]=problem
    
    def get_List_of_question(self):
        return self.__questionDict

