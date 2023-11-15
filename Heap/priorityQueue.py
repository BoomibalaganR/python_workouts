from maxHeap import MaxHeap 

class PriorityQueue:
    
    def __init__(self):
        self.pqueue = []
    
    def pop(self): 
        
        val = MaxHeap.pop(self.pqueue, len(self.pqueue)) 
        if val is not None: 
            return val
        print("priority queue is empty")

    
    def push(self, val):
        MaxHeap.push(self.pqueue, val)
        
        
    def get_max(self):
        if len(self.pqueue) != 0:
            return self.pqueue[0]
        print("queue is empty...") 
        

# main 
pq = PriorityQueue()


