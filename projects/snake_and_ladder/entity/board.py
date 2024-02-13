class Board: 
    
    def __init__(self, size):  
        self.__size = size*size 
        self.__snake = dict() 
        self.__ladder = dict()  
        self.__player = list() 
        
        self.add_snake() 
        self.add_ladder()
    
    
    def get_cur_player(self): 
        return self.__player.pop(0)
    
    def add_player(self, player): 
        self.__player.append(player)
    
    def add_snake(self):  
        snake={14: 4, 27: 21, 34: 10} 
        for start, end in snake.items(): 
           self.__snake[start] = end
    
    def is_snake(self, position): 
         return self.__snake.get(position) 
       
    def add_ladder(self): 
        ladder = {5: 16, 15: 28} 
        for start, end in ladder.items(): 
           self.__ladder[start] = end 
       
    def is_ladder(self, position): 
        return self.__ladder.get(position)



board = Board(6) 
