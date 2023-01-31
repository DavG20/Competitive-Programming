def Sol():
    
    row , col = list(map(int, input().split()))
    
    answer=""
    
    inbound = lambda x , y : 0 <= x < row and 0 <= y <col
    
    directions = [(0,1), (1,0),(-1,0),(0,-1)]
    
    
    grid = []
    
    for _ in range(row):
        
        grid.append(list(input()))
        
    
    
    for i in range(row):
        
        for j in range(col):
            isValid_letter=True
            
            
            
            
            for dx , dy in directions:
                curr_x = i + dx  
                curr_y=j + dy
                
                while inbound(curr_x,curr_y) and grid[i][j]!=grid[curr_x][curr_y]:
                    curr_x  = curr_x + dx  
                    curr_y = curr_y + dy
                    
                if inbound(curr_x,curr_y):
                    isValid_letter=False
                    break
            if isValid_letter:
                answer+=grid[i][j]
    print(answer)                
Sol()