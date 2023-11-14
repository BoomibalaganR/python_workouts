from doublyLinkedList import DoublyLinkedList 


dList = DoublyLinkedList()   


dList.display() 

dList.insert_at_begin(3)
dList.insert_at_begin(6)

dList.insert_at_end(7)  
dList.display()  


dList.insert_at_pos(2,8)
dList.display() 
input()

dList.delete_at_begin()
dList.display() 
dList.reverse()

dList.delete_at_end()
dList.display() 
dList.reverse() 

dList.delete_at_end()
dList.display() 
dList.reverse() 

