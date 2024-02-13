
def simplifyPath(path): 
    
        path = path.split("/") 
        stack = list() 
      
        for p in path: 
            
            if p == ".." and len(stack) != 0: 
                stack.pop() 
            elif p != "" and p != ".." and p != ".":
                stack.append(p) 
            
        return "/" + "/".join(stack) 
    
    

path = "/../..ga/b/.f..d/..../e.baaeeh./.a"  

print(simplifyPath(path))