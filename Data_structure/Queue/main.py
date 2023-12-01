from linearQueue import Queue

   
queue = Queue(2) 

queue.enqueue(3) 
queue.enqueue(5) 

queue.dispaly()  

print("\nget front: ",queue.getFront())
print("get rear: ",queue.getRear())

print("\ndequeued element: ",queue.dequeue()) 
print("dequeued element: ",queue.dequeue())  
print("dequeued element: ",queue.dequeue())
queue.dispaly() 