from binary_searchTree import BinarySearchTree  
from avl_Tree import AVLtree

avlTree = AVLtree()   

lst = [20,20,10,5,2,30,45,44,50,60]
# lst = [50,20,60,10,30,40]

for i in range(len(lst)): 
    avlTree.insert(lst[i])    
   

avlTree.in_order(avlTree.root)  








