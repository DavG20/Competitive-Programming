class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dir_ver = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        inbound = lambda x , y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        target = (len(grid) - 1 ,len(grid[0]) - 1 )
        
        queue = deque([(0,0)])
        
        
        visited =  set([(0,0)])
        
        
        if  grid[0][0]:
            
            return -1
        
        if len(grid) == 1:
            return 1
        
        count = 1
        
        while queue:
            
            curr_lev = len(queue)
            
            count += 1
            
            for i in range(curr_lev):
                
                curr_x , curr_y = queue.popleft()
                
                
                
                for dx , dy in dir_ver :
                    
                    if inbound(curr_x + dx , curr_y + dy) and grid[curr_x + dx][curr_y + dy] == 0 :
                        
                        if target == (curr_x + dx , curr_y + dy) :
                            
                            return count
                        
                        if (curr_x + dx , curr_y + dy) not in visited:
                            
                            visited.add((curr_x + dx , curr_y + dy))
                            
                            queue.append((curr_x + dx , curr_y + dy))
                            
            
                        
                    
        return -1
                
                        
                        
                