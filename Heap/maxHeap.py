import math

class MaxHeap:
    
    def __init__(self):
        self.heap= []  
        self.size = 0
        
    
    # get maximum element
    def get_max(self):
        if len(self.heap) != 0:
            return self.heap[0]
    
    
    # delete the element from max heap
    def delete_element(self):  
       
        if self.size == 0:
            return
        v = self.heap[0] 
        
        self.heap[0] = self.heap[self.size-1]
        del self.heap[self.size-1] 
        self.size-=1 
        
        self.__adjust_top_down(0) 
        return v
        
   
   
    # adjust max heap condition from top-down when delete the element
    def __adjust_top_down(self, parent):  
       
        while parent < self.size:  
            
            print(self.heap)
            parent =  self.to_satisfy_heap(parent) 
            if parent is None: 
                 return
                
    
    # insert the element into max heap
    def insert_element(self, element): 

        self.heap.append(element) 
        self.size+=1 
        
        if self.size == 0:
            return  
        
        self.__adjust_buttom_up()       
            
    
    # adjust max heap condition from buttom-Up when insert the element
    def __adjust_buttom_up(self): 
      
        child = self.size-1
        parent = math.ceil(child/2)-1  
        
        while parent >= 0:     
            
            if self.heap[parent] < self.heap[child]:  
                self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent]  
                child = parent
                parent = math.ceil(child/2)-1  
            else:
                return   
    
        
    # heap condition 
    def to_satisfy_heap(self, parent):  
        
            left = 2*parent+1 
            right = 2*parent+2  
        
            if right < self.size:   
                
                if self.heap[left] < self.heap[right] and self.heap[parent] < self.heap[right]:
                    self.heap[parent], self.heap[right] = self.heap[right], self.heap[parent]
                    return right  
                elif  self.heap[right] < self.heap[left] and self.heap[parent] < self.heap[left]: 
                    self.heap[parent], self.heap[left] = self.heap[left], self.heap[parent]
                    return left
               
                
            elif left < self.size: 
                 if  self.heap[parent] < self.heap[left]:
                    self.heap[parent], self.heap[left] = self.heap[left], self.heap[parent]
                    return left 
            
            return None
        


   



