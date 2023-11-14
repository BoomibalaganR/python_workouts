from maxHeap import MaxHeap 

hp = MaxHeap() 

lst = [1,2,3,4,5,6,7,9]   

# create heap
for i in lst:
     hp.insert_element(i)  
print(hp.heap) 
  

  

# delete element 
for i in range(9): 
    print("\n------------------------------")
    print("heap size: ",hp.size) 
    print("before: ",hp.heap)
    hp.delete_element()  
    print("after: ",hp.heap)


