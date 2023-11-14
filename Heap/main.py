from maxHeap import MaxHeap 


lst = [1,2,3,4,5]   
print(lst)
MaxHeap.heapify(lst)
print("heap : ",lst) 
MaxHeap.heap_push(lst, 6)
print(lst)
exit()

# delete element 
for i in range(9): 
    print("\n------------------------------")
    print("heap size: ",hp.size) 
    print("before: ",hp.heap)
    hp.delete_element()  
    print("after: ",hp.heap)


