
class AVLtree: 
    
    def __init__(self): 
       self.root = None

    class __Node: 
        
        def __init__(self, data):  
            self.left = None
            self.data = data 
            self.right = None   
            self.height = 0 
            
        
        # helper method 
    def insert(self, data):   
        self.root = self.__insert(self.root, data) 
       
    # insert the data to tree 
    def __insert(self, root, data): 
      
        if root is None:  # insert the node
            return self.__Node(data) 
        
        if data < root.data: 
           root.left = self.__insert(root.left, data) # take left 
        elif root.data < data: 
           root.right =  self.__insert(root.right, data) # take right 
        
    
        root.height = max(self.get_height(root.left), self.get_height(root.right))+1 
    
        balfact = self.get_height(root.left)-self.get_height(root.right) 
        
        # RR 
        if balfact == -2 and root.right.data < data : 
           return self.left_rotate(root)
        
        #RL 
        if balfact == -2 and root.right.data > data: 
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        
        #LL 
        if balfact == 2 and root.left.data > data: 
          return self.right_rotate(root)
      
        #LR 
        if balfact == 2 and root.left.data < data: 
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
       
        return root
    
    
    #left rotate 
    def left_rotate(self,root):
        Y = root.right 
        t1 = Y.left 
        
        Y.left = root
        root.right = t1
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right)) 
        Y.height = 1 + max(self.get_height(Y.left),self.get_height(Y.right)) 

        return Y
        
    
    #right rotate
    def right_rotate(self,root):
        
        Y = root.left 
        t1 = Y.right 
        Y.right = root
        root.left = t1

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right)) 
        Y.height = 1 + max(self.get_height(Y.left),self.get_height(Y.right)) 

        return Y
    
    # get height of the root 
    def get_height(self,root):
        if root is None: 
            return -1
        return root.height 
    
    
     #display tree in order traversal         
    def in_order(self, root): # Left --> Root --> Right
        
        if root is None:
            return
        self.in_order(root.left) 
        print(root.data,"hight: ",root.height)  
        self.in_order(root.right) 
   