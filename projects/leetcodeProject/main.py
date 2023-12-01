from model.Db.Database import *   
from API.Request_API import Request 
from view import topics 
from view import all_problem 
import view.problem_Statement as prb
from model.entity.Topic import Topic

#intialise the database 
Database.intialise()  



topicList = Request.get_listOf_topics()


while(True): 
    topics.display(topicList) 
    choice = int(input("enter topic ID: ")) 
    
    if(choice == 0 ): 
        print("\n\nThanks to visit.!!!\n")
        break
    if choice > len(topicList):
        print("enter valid ID {}to{}".format(1,len(topicList))) 
        continue
        
    topicObj = Request.get_AllProblemByID(topicList[choice-1]) #get topic object from db
    Dict_AllQuestion = topicObj.get_List_of_question()
    
    
    
   
    while(True):  
        all_problem.display(Dict_AllQuestion,topicObj.get_topicName())  
    
        print("1. open to solve problem") 
        print("2. back")  
        choice = int(input("enter Your choice: "))
        
        if (choice == 1):  
            
            while(True):
                id = int(input("Enter problem ID: "))  
                if(id not in Dict_AllQuestion): 
                    print("\nEnter valid problem ID...")
                    continue
                break  
            
            prb.display(Dict_AllQuestion.get(id)) 
            input("if go Back, Press Enter...")
         
        elif (choice == 2):
            break
        else:
            print("Enter valid choice")
            continue
 



    
    

