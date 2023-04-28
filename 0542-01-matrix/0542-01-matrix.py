class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        dir_vec = [(1,0) , ( -1 , 0), (0 , 1 ), (0 , -1)]
    
        inbound = lambda x , y : 0 <=  x < len(mat) and 0 <= y < len(mat[0])
        
        
        queue = deque([])
        
        visited = set([])
        
        
        for i in range(len(mat)):
            
            for j in range(len(mat[0])):
                
                if not mat[i][j]:
                    queue.append((i , j))
                    visited.add((i , j))
                    
        
        count = 1
        while queue :
            
            cur_lev = len(queue)
            
            
            
            
            for i in range(cur_lev):
                
                curr_x , curr_y = queue.popleft()
                
                 
                 
                
                
                for dx , dy in dir_vec :
                    
                    if inbound(curr_x + dx , curr_y + dy ) and (curr_x + dx , curr_y + dy ) not in visited:
                        
                        # if mat[curr_x + dx][curr_y + dy ]:
                            
                        mat[curr_x + dx][curr_y + dy ] = count

                        queue.append((curr_x + dx, curr_y + dy))

                        visited.add((curr_x + dx, curr_y + dy))

            count += 1
                            
                    
                    
        
        
        return mat
                        
                
                
                
                
                