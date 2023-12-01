class LinkedList: 
    
    def __init__(self):
       self.__head = None 
       
    class __Node: 
        
        def __init__(self):
            self.data = None
            self.next = None    
            
     
    # display the linked list
    def display(self): 
       
        temp_head = self.__head 
        while temp_head is not None:
            print(temp_head.data,end=' ') 
            temp_head = temp_head.next 
        print()
            
            
    # insert value at beginning
    def insert_at_begin(self, value): 
        
        if self.__head is None: 
            new_node = self.__Node() 
            new_node.data = value 
            self.__head = new_node 
        else: 
            new_node = self.__Node() 
            new_node.data = value 
            
            new_node.next = self.__head
            self.__head = new_node
        
    
    
    # insert the value at end 
    def insert_at_end(self,value): 
        
        if(self.__head is None):
            self.insert_at_begin(value)  
            return
        
        temp_head = self.__head
        while temp_head.next is not None: # traverse to end
            temp_head = temp_head.next
        
        new_node = self.__Node() 
        new_node.data = value 
        temp_head.next = new_node
                
    
    # insert at any postion 
    def insert_at_position(self, pos, val):
           
        if(pos < 0):
            return 
        
        if (self.__head is None  and 0 < pos):
            print("list is empty..")  
            return
        if pos == 0: 
            self.insert_at_begin(val)
            return  
        
        temp_head = self.__head 
        for i in range(pos-1): 
            if(temp_head.next is None):
                self.insert_at_end(val) 
                return
            temp_head = temp_head.next 
            
        new_node = self.__Node() 
        new_node.data =val 
        new_node.next = temp_head.next 
        
        temp_head.next= new_node 
        print("successfuly inserted pos at {} val {}".format(pos,val))
  
    
    #delete at begin 
    def delete_at_begin(self):
        
        if self.__head is None:
            print("linked list is empty") 
            return 
        self.__head  = self.__head.next 
        
    
    #delete at end 
    def delete_at_end(self):  
        
        if self.__head is None:
            print("linked list is empty") 
            return
        
        if self.__head.next is None: 
            self.__head = None 
            return
        
        temp_head = self.__head   
        
        while temp_head.next.next is not None:   
            temp_head = temp_head.next
        
        del_val = temp_head.next.data
        temp_head.next = None 
        
        return del_val
        
    
    # delete at any pos 
    def delete_at_pos(self,pos):
        
        if(pos < 0):
            return  
    
        if(pos == 0):
            self.delete_at_begin() 
            return 

        temp_head = self.__head 
        for i in range(pos-1): 
            if(temp_head is None):
                return
            temp_head = temp_head.next 
            
        temp_head.next = temp_head.next.next
    
    
    # reverse the list 
    def reverse(self): 
        if(self.__head is None):
            return 
        
        prev_node = None 
        next_node = self.__head 
        cur_node = self.__head 
        
        while(next_node is not None):
           next_node = cur_node.next 
           cur_node.next = prev_node 
           prev_node = cur_node  
           
           cur_node = next_node
           
        self.__head = prev_node