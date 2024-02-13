from board import Board 
from player import Player 
from dice import Dice

class Game:
    
    def __init__(self): 
        self.board = Board(6) 
        self.board.add_player(Player("rolex"))
        self.board.add_player(Player("boomi")) 
        self.history = list()
    
    def start_game(self): 
         
        while(True): 
            cur_player = self.board.get_cur_player() 
            self.board.add_player(cur_player) 
            
            old = cur_player.get_current_pos()
            step =  Dice.roll()   
            new_pos = cur_player.move(step) 

               
            if new_pos == 36:
                 return  
             
            snake_pos = self.board.is_snake(new_pos) 
            if snake_pos is not None: 
                cur_player.set_current_pos(snake_pos)  
                d  = {"cur_player": cur_player.name,"old_pos": old, "step": step, "new_pos": cur_player.get_current_pos(), "is_snake": "yes" , "after ": cur_player.get_current_pos()} 
                self.history.append(d)
               
                continue
            
            ladder_pos = self.board.is_ladder(new_pos) 
            if ladder_pos is not None: 
                cur_player.set_current_pos(ladder_pos) 
              
                d  = {"cur_player": cur_player.name,"old_pos": old, "step": step, "new_pos": cur_player.get_current_pos(), "is_ladder": "yes" , "after ": cur_player.get_current_pos()} 
                self.history.append(d)
                continue 
            
           
            d  = {"cur_player":cur_player.name,"old_pos": old, "step": step, "new_pos": cur_player.get_current_pos(), "no_ladder and snake": "yes"} 
            self.history.append(d)
          
           
game = Game() 

game.start_game()  

for h in game.history: 
    print(h) 
    