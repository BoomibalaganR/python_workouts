from queue import Queue

# graph represent using ajancency matrix
class Graph1: 
    
    # initialise the ajacency matrix with number of vertex
    def __init__(self, numVertex):
        self.aj_mtx = [[0 for col in range(numVertex+1)] for row in range(numVertex+1) ]  
        
    
    # set vertex with corresponding edges (optional weight)
    def set_vertex(self, vtx, edge, weight = 1):
        self.aj_mtx[vtx][edge] = weight
    
    
    # traverse breath first search
    def traverse_bfs(self, st_vertex): 
        q = Queue()  
        
        # to track visited vertex, intially all vertexes not visited
        visited = [False for i in range(len(self.aj_mtx))]  
       
        # store search element
        res=[] 
     
        # put given starting-vertex into queue 
        # And set visited that vertex
        q.put(st_vertex) 
        visited[st_vertex] = True 
        
    
        while q.empty() is not True:  
            
            # get vertex from the queue and
            # append into res list
            vertex = q.get()   
            res.append(vertex)        
            
            # explore all edges corresponding to vertex
            for edge in range(len(self.aj_mtx[0])):  
                
                # only explore not visited vertex 
                # And weight greater than 1
                if 0 < self.aj_mtx[vertex][edge] and visited[edge] is False: 
                    
                    # put not visited vertex into queue 
                    # set visited
                    q.put(edge)
                    visited[edge] = True 
        return res



   # helper
    def traverse_dfs(self, st_vertex):  
        
        # initialise the visited list for 
        # to track which vertex not visited   
        visited = [False for i in range(len(self.aj_mtx[0]))]   
        
        # to store search element
        res = []
        
        # call actuall dfs method
        self.__traverse_dfs(visited, st_vertex, res)  
        print(res)

        # return result
        return res
        
    
    # traverse depth first search using recurrence
    def __traverse_dfs(self, visited, vertex, res):
          
        # check vertex is visited or not
        # if visited simply return otherwise continue.
        if visited[vertex] is True:
              return 
          
        # set current vertex is visited and
        # append the current vertex to result list
        visited[vertex] = True 
        res.append(vertex)
        
        # explore all edge current vertex
        for edge in range(len(self.aj_mtx[0])):
            
            # check weight of current vertext greater than 1
            if 0 < self.aj_mtx[vertex][edge]: 
                
                # call itself with current not visited edge
                self.__traverse_dfs(visited, edge, res)  
        
        
    

