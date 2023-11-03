class Stack:
    
    def __init__(self,size = 10): 
        self.__size = size
        self.__stack = [ None for i in range(size)] 
        self.__top = -1
      
    # push element into list
    def push(self,val): 
        
        if(self.isFull()):
            print("stack is full...") 
        else: 
            self.__top+=1 
            self.__stack[self.__top] = val 
            print("successfully pushed value...")
        
    
    # delete element in the list
    def pop(self): 
        
        if(self.isEmpty()):
            print("stack is empty..")
            return 
        val = self.peek()
        self.__top-=1 
        return val
      
        
    # return top of the stack
    def peek(self):
        
        if(self.isEmpty()):
            print("stack is empty..")
            return
        
        return self.__stack[self.__top] 
    
    
    def isEmpty(self):
        return self.__top == -1 
    
    
    def isFull(self):
        return self.__size-1 <= self.__top 
    
    
    # display the stack element
    def display(self): 
        
        if(self.isEmpty()):
            print("stack is empty..")
            return
      
        for i in range(0,self.__top+1):
            print(self.__stack[i],end=' ')

