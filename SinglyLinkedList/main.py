from linkedList import LinkedList 

linkedList = LinkedList()  
    
while(True):
    
    print("\n1. insert at begin") 
    print("2. insert at end") 
    print("3. insert at any position") 
    print("4. delete at begin") 
    print("5. delete at end") 
    print("6. delete at any position") 
    print("7. reverse the list")
    print("8. display")  
    print("9. exit")
    print("-----------------------------------")
    
    choice = int(input("enter your choice: ")) 
    
    if choice == 1:
        data = int(input("Enter the data: ")) 
        linkedList.insert_at_begin(data)
    
    elif choice == 2: 
        data = int(input("enter the data: "))
        linkedList.insert_at_end(data) 
    
    elif choice == 3:
       pos = int(input("enter the position: "))
       data = int(input("enter the data: ")) 
       linkedList.insert_at_position(pos, data)
    
    elif choice == 4:
        linkedList.delete_at_begin()
    
    elif choice == 5:
        linkedList.delete_at_end() 
    
    elif choice == 6: 
        pos = int(input("enter the position: "))
        linkedList.delete_at_pos(pos)

    elif choice == 7:
        linkedList.reverse() 
            
    elif choice == 8:
        linkedList.display() 
        
    elif choice == 9:
        break
    
    else: 
        print("enter valid choice")
    
    
  