from binaryTree import BinaryTree 

biTree = BinaryTree(1) 

biTree.insert_left(biTree.root, 2)   
biTree.insert_right(biTree.root, 3)  

biTree.insert_left(biTree.root.right, 4) 

biTree.pre_order(biTree.root) 
print()
biTree.in_order(biTree.root)


