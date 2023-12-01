from model.entity.Problem import Problem

def display(Dict_AllQuestion,topicName): 
    
     
    print("\nTopic: "+topicName)
    print("------------------------------------------------------") 
    print("ID\tTitle\t\t\t\tDifficulty")
    print("------------------------------------------------------\n") 
    for val in Dict_AllQuestion.values(): 
       print(Problem.get_ID(val),"\t",Problem.get_title(val),"\t",Problem.get_difficult_level(val))
    
    print("\n------------------------------------------------------") 