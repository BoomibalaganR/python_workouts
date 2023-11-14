import math

class MaxHeap: 
    
    
    @staticmethod
    def push(heap, val):
        heap.append(val)   
        if(1 < len(heap)):
             MaxHeap.__adjust_buttom_up(heap)
        return True
    
    @staticmethod
    def pop(heap): 
        
        size = len(heap)
        if size == 0:
            return None
        val = heap[0] 
        
        heap[0] = heap[size-1]
        del heap[size-1]  
        MaxHeap.__heapify(heap, 0) 
        return val 
    
    
    # adjust max heap condition from buttom-Up when insert the element  
    @staticmethod
    def __adjust_buttom_up(heap): 
        print("size: ",len(heap))
        child = len(heap)-1
        parent = math.ceil(child/2)-1  
        
        while parent >= 0:     
            
            if heap[parent] < heap[child]:  
                heap[parent], heap[child] = heap[child], heap[parent]  
                child = parent
                parent = math.ceil(child/2)-1  
            else:
                return    
            
    
    @staticmethod
    def heapify(heap):
        for parent in range(len(heap)-1, -1, -1):
            MaxHeap.__heapify(heap, parent)
       
    
    @staticmethod
    def __heapify(heap, parent): 
  
        while parent is not None: 
            parent = MaxHeap.to_satisfy_heap(heap, parent) 
              
        
    # heap condition  
    @staticmethod
    def to_satisfy_heap(heap, parent):  
        
            left = 2*parent+1 
            right = 2*parent+2  
            size = len(heap)
            
            if right < size:   
                
                if heap[left] < heap[right] and heap[parent] < heap[right]:
                    heap[parent], heap[right] = heap[right], heap[parent]
                    return right  
                elif  heap[right] < heap[left] and heap[parent] < heap[left]: 
                    heap[parent], heap[left] = heap[left], heap[parent]
                    return left
               
                
            elif left < size: 
                 if  heap[parent] < heap[left]:
                    heap[parent], heap[left] = heap[left], heap[parent]
                    return left 
            
            return None
        


 
   

