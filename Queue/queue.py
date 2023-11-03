
class Queue: 
    
    def __init__(self,size=10):
        self.__size = size 
        self.__queue = [None for i in range(size)] 
        self.__rear = -1


    def enqueue(self, val):
        
        if(self.isFull()):
            print("queue is full") 
            return 
        
        self.__rear+=1
        self.__queue[self.__rear] = val 
        print("successfully Enqueued..")
    
    
    def dequeue(self):
        
        if(self.isEmpty()):
            print("queue is empty")  
            return 
        val = self.__queue[0]  
        # shift element left one position
        i = 0
        while(i < self.__rear):
            self.__queue[i] = self.__queue[i+1] 
            i+=1

        self.__rear-=1 
        return val 
    
            
    def getFront(self):
        return self.__queue[0]
    
    
    def getRear(self):
        return self.__queue[self.__rear]
    
    
    def isEmpty(self):
        return self.__rear == -1
    
    
    def isFull(self):
        return self.__size-1 <= self.__rear  
    
    
    def dispaly(self): 
        if self.isEmpty():
            return
        
        for i in range(self.__rear+1):
            print(self.__queue[i],end=' ')
    
 