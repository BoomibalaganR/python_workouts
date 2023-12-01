from queue import Queue

# graph represent using ajancency list
class Graph2: 
    
    def __init__(self, node):
        self.aj_list = [[] for i in range(node+1) ]  
       
    
    def insert(self, node, edge):
        self.aj_list[node].append(edge) 
    
    
    # traverse breath first search
    def traverse_bfs(self, st_Node): 
        q = Queue() 
        visited = [False for i in range(len(self.aj_list))]
       
        q.put(st_Node) 
        visited[st_Node] = True 
       
        while q.empty() is not True: 
            
            node = q.get() 
          
            for i in self.aj_list[node]:
               if visited[i] is False:
                    q.put(i)  
                    visited[i] = True
            print(node,end=" ") 
          
 
   # helper
    def traverse_dfs(self, st_node):    
        visited = [False for i in range(len(self.aj_list))]  
        res = []
        self.__traverse_dfs(visited, st_node, res)  
        return res
        
    
    # traverse depth first search   
    def __traverse_dfs(self, visited, node, res):
          
        if visited[node] is True:
              return 
        visited[node] = True 
        res.append(node)
        
        for i in self.aj_list[node]:
            self.__traverse_dfs(visited, i, res)  
        
        
    

