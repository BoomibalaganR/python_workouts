def dfs(mtx, visited, row, col):
    
    if mtx[row][col] == 0 or visited[row][col] is True:
        return
    
    visited[row][col] = True

    for i in range(-1,2):
       for j in range(-1,2): 
            nrow =  row+i 
            ncol = col+j  
            if 0 <= nrow and nrow < len(mtx) and 0 <= ncol and ncol < len(mtx[0]):
                dfs(mtx, visited, nrow, ncol )        


#main 
mtx = [ [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1] ] 

visited = [[False for col in range(len(mtx[0]))] for row in range(len(mtx))] 
no_island = 0

for row in range(len(mtx)):
    for col in range(len(mtx[0])):

        if mtx[row][col] == 1 and visited[row][col] is False:             
            no_island+=1
            dfs(mtx, visited, row, col)  
            
print(no_island)