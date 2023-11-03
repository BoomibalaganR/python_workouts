class BinaryTree: 
 
    def __init__(self,val):
        self.root = self.__Node(val) 
 

    class __Node: 
        
        def __init__(self, data):  
            self.left = None
            self.data = data 
            self.right = None   
            
            
    def insert_left(self, root, data): 
        root.left = self.__Node(data)   
    
    
    def insert_right(self, root, data):
        root.right = self.__Node(data)     
    
    
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
        self.pre_order(root.left) 
        print(root.data, end=' ') 
        self.pre_order(root.right) 
    
    
    
    
    
    
        
        
        