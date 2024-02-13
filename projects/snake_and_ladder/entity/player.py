class Player:
    
    def __init__(self, name):  
        self.name = name
        self.__current_pos = 0 
        self.history = list()
    
    
    def move(self, steps): 
        
        temp = self.__current_pos + steps  
       
              
        if temp < 36: 
            self.__current_pos+=steps 
            return self.__current_pos 
        
        elif(temp == 36): 
            print("won") 
            return 36
    
     
    def get_current_pos(self): 
        return self.__current_pos   
    
    def set_current_pos(self, new_pos): 
        self.__current_pos = new_pos;