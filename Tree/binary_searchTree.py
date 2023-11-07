from queue import Queue

class BinarySearchTree: 

    def __init__(self): 
       self.root = None

    class __Node: 
        
        def __init__(self, data):  
            self.left = None
            self.data = data 
            self.right = None   
                
    
    # insert the data to tree 
    def insert(self, root, data): 

        if self.root is None: 
            self.root = self.__Node(data) 
            return   
            
        if root is None:  
            return self.__Node(data) 
        
        if data < root.data: 
           root.left = self.insert(root.left, data) # take left 
        elif root.data < data: 
           root.right =  self.insert(root.right, data) # take right 
           
        return root
    
    def delete(self, data):
        self.root = self.__delete(self.root, data)

    # delete the node in tree 
    def __delete(self, root, data):  
        
        if root is None:  
            print("\nno element found")
            return  

        if(data < root.data):
            root.left = self.__delete(root.left, data)
        elif(root.data < data): 
           root.right = self.__delete(root.right, data)  
           
        else:
            if( root.right is None): 
                 return root.left
            elif root.left is None:
                return root.right 
            else:  
                min_val = self.min(root.right)
                root.data = min_val
                root.right = self.__delete(root.right, min_val)
               
        return root  
     
     
    # find minimum value 
    def min(self, root):

        min_val = root.data
        while root is not None: 
            min_val = root.data
            root = root.left
        return min_val  
    
    
    # level order traversal  
    def level_order(self, root):  
        
        if root is None: 
            print("no element to dispaly") 
            return
        q = []
        q.append(root) 
      
        while(len(q) != 0): 
            
            root = q.pop(0) 
            print(root.data,end=" ")  
            
            if root.left is not None:
                q.append(root.left)  
            if root.right is not None: 
                q.append(root.right)  
   
    
    # display tree pre order traversal
    def pre_order(self, root): # Root --> Left --> Right
        
        if root is None:
            return 
        print(root.data, end=' ') 
        self.pre_order(root.left)
        self.pre_order(root.right) 
    
    
    #display tree in order traversal         
    def in_order(self, root): # Left --> Root --> Right
        
        if root is None:
            return
        self.in_order(root.left) 
        print(root.data, end=' ') 
        self.in_order(root.right) 
    
    
    # display tree post order traversal         
    def post_order(self, root): # Left --> Right --> Root 
        
        if root is None:
            return
        self.post_order(root.left) 
        self.post_order(root.right) 
        print(root.data, end=' ')  