class CircularLinkedList: 
   
    def __init__(self):
       self.__head = None 
       self.__tail = None
    
    class __Node: 
        
        def __init__(self):
            self.data = None
            self.next = None 
            

     # insert value at beginning
    def insert_at_begin(self, value): 
        
        if self.__head is None: 
            new_node = self.__Node() 
            new_node.data = value  
            new_node.next = new_node 
        
            self.__head = new_node  
            self.__tail = new_node
        else: 
            new_node = self.__Node() 
            new_node.data = value 
            
            new_node.next = self.__head
            self.__head = new_node 
            self.__tail.next = new_node
        print("successfully inserted at begin....")    
    
    
    # insert at end 
    def insert_at_end(self, val):  
        
        if(self.__head is None):
            self.insert_at_begin(val)  
            return
     
        new_node = self.__Node() 
        new_node.data = val 
        new_node.next = self.__tail.next 
        
        self.__tail.next = new_node 
        self.__tail = new_node      
        print("successfully inserted at end..") 
    
    
    # display the circular list
    def display(self):
        
        if(self.__head is None):
            print("no element to display..")
            return 
                
        temp_head = self.__head  
        while(temp_head ): 
            print(temp_head.data,end=' ')
            temp_head = temp_head.next 
            if(temp_head is self.__head): 
                print()
                return
    