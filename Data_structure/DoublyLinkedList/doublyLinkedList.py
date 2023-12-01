
class DoublyLinkedList: 

    def __init__(self):
        self.__head = None
        self.__tail = None
        
    class __Node:  
    
        def __init__(self):
            self.prev = None 
            self.data = None 
            self.next = None 
            
    
    # insert at beginning
    def insert_at_begin(self,val):
        
        if self.__head is None: 
            new_node = self.__Node() 
            new_node.data = val 
            self.__head = new_node 
            self.__tail = new_node
        else: 
            new_node = self.__Node() 
            new_node.data = val 
            
            self.__head.prev = new_node
            new_node.next = self.__head 
            self.__head = new_node  
        print("successfully inserted at begin: ",self.__head.data)
           
           
     # insert at endding      
    def insert_at_end(self,val):
        
        if self.__head is None: 
            print("list is empty")
            return 
        
        new_node = self.__Node() 
        new_node.data = val 
        new_node.prev = self.__tail
        
        self.__tail.next = new_node 
        self.__tail = new_node 
        print("\nsuccessfully inserted at end..",self.__tail.data) 
    
    
    # insert at any pos 
    def insert_at_pos(self,pos,val):
        
        if(pos == 0):
            self.insert_at_begin(val) 
            return 

        temp_head = self.__head
        for i in range(pos): 
            temp_head = temp_head.next 
        
        new_node = self.__Node()  
        new_node.data = val 
          
        new_node.next = temp_head 
        new_node.prev = temp_head.prev 
        
        temp_head.prev.next = new_node 
        temp_head.prev = new_node
             
        
    
    # delete node at begin
    def delete_at_begin(self):
        
        if(self.__head is None):
            print("\n list is Empty") 
            
        elif(self.__head.next is None):
            self.__head = None 
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None 
            print("\nsuccessfully deleted at begin..")
    
    
    # delete node at end
    def delete_at_end(self):
        
        if(self.__head is None):
            print("list is empty")
        elif (self.__head.next is None):
            self.__head = None 
            self.__tail = None
        else: 
            self.__tail = self.__tail.prev  
            self.__tail.next = None 
        print("\nsuccessfully deleted at end..")
    
    
    # display the list
    def display(self):
        
        if(self.__head  is None):
            print("no element to display") 
            return 
        
        temp = self.__head
        while(temp):
            print(temp.data,end=' ') 
            temp = temp.next 
        print()  
            
            
    # reverse the dList
    def reverse(self):
        
        if(self.__head is None):
            print("no element to display")
            return 
        
        temp = self.__tail 
        print()
        while(temp):
            print(temp.data,end=' ')
            temp = temp.prev 
        print()