class Problem:
     __idCounter = 0 
     
     def __init__(self) : 
          Problem.__idCounter+=1 
          
          self.__ID = Problem.__idCounter
          self.__title = None 
          self.__problem_stm = None 
          self.__testCase = None 
          self.__difficult_level = None 
          
     def get_ID(self):
          return self.__ID 

     def get_title(self):
          return self.__title 
     def set_title(self,title):
          self.__title = title
     
     def get_problem_statement(self):
          return self.__problem_stm  
     def set_problem_statement(self, problemStatement):
          self.__problem_stm = problemStatement
     
     def get_testCase(self):
          return self.__testCase  
     def set_testCase(self,testCase):
          self.__testCase = testCase
     
     def get_difficult_level(self): 
          return self.__difficult_level  
     
     def set_difficult_level(self,level):
          self.__difficult_level = level.title()
     
          