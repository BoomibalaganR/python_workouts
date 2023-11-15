from ..entity.Problem import Problem 
from ..entity.Topic import Topic

class Database: 
  
  DictOf_Topics={}  
  

  #intialise some data  
  @staticmethod
  def intialise(): 
    
    #Arrray Topic
    array = Topic("array") 
   
    #creat question
    arrQues1 = Problem()  
    arrQues1.set_title("Find Next Greatest Number") 
    arrQues1.set_difficult_level("easy") 
    arrQues1.set_problem_statement("find nextGreatest Number in given Array: \n\nnums = [1, 2, 3, 4, 5]\nOutput: [2, 3, 4, 5, -1]") 
    arrQues1.set_testCase("TestCase 1:\n nums = [2, 4, 5, 6]\nOutput: [4, 5, 6, -1]")  
   
    #add question under array Topic
    array.add_question(arrQues1)
    
    #-----------------------------------------#
  
    #String Topic 
    string = Topic("string") 
    
    #create question
    strQues1 = Problem() 
    strQues1.set_title("reverse the given String") 
    strQues1.set_difficult_level("easy") 
    strQues1.set_problem_statement('Reverse the Given String \n\nstr = "pythonProgramming" \nOutput: "gnimmargorPnohtyp" ') 
    strQues1.set_testCase('TestCase 1: \n str = "LeetCode" \n Output: "edoCteeL"') 
    
    #add question under String Topic 
    string.add_question(strQues1) 

    #----------------------------------------- 
    # Add all topic into database (dictionary)
    Database.DictOf_Topics[array.get_topicName()] = array 
    Database.DictOf_Topics[string.get_topicName()] = string  
    
    
    print("Successfully intialise Data..!!!\n")
    
    
  