def sol():
    
    t = int(input())
    
    directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        
    inbound = lambda x , y : 0 <= x < n and 0 <= y < m
    
    for _ in range(t):
        
        n , m = list(map(int, input().split()))
        
        
        grid =  []
        
        for  _ in range(n):
            
            grid.append(list(map(int, input().split())))
        
        
        
        
        
        max_sum = 0
        for i in range(n):
            
            for j in range(m):
                temp_sum = grid[i][j]
                
                             
                for dx , dy in directions:
                    curr_x , curr_y = i + dx  , j + dy
                    
                    while inbound(curr_x , curr_y):
                        temp_sum += grid[curr_x][curr_y]
                        curr_x += dx 
                        curr_y += dy
                if temp_sum > max_sum:
                    max_sum = temp_sum
        print(max_sum)
                        

                
                
        
sol()