from binary_searchTree import BinarySearchTree 

biTree = BinarySearchTree()   

lst = [20,10,5,2,30,45,44,50,60]

for i in range(len(lst)):
    biTree.insert(biTree.root, lst[i])  

biTree.level_order(biTree.root) 
biTree.delete(20)
print()
biTree.level_order(biTree.root)






