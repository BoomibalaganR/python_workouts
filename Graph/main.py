from graph1 import Graph1
from graph2 import Graph2 


# graph represent ajacency matrix  
num_vertex = 7
bi_graph1 = Graph1(num_vertex) 

lst = [(1, 6), (1, 2), (2, 3), (2, 4), (3, 2), (4, 2), (4, 5), (5, 6),(5, 4), (6, 7),(6, 1), (6, 5), (7, 6)]

for tp in lst: 
   bi_graph1.set_vertex(tp[0],tp[1]) 

print(bi_graph1.aj_mtx)

bi_graph1.traverse_dfs(6)


exit()









# graph represent ajacency list
bi_graph = Graph2(7) 

lst = [(1, 6), (1, 2), (2, 3), (2, 4), (3, 2), (4, 2), (4, 5), (5, 6),(5, 4), (6, 7),(6, 1), (6, 5), (7, 6)]

for tp in lst: 
   bi_graph.insert(tp[0],tp[1]) 

print(bi_graph.aj_list) 

print(bi_graph.traverse_dfs(6))