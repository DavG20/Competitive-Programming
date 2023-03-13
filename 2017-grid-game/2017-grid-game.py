class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0]) 
        
        pref_sum_0 = [0 for _ in range(n + 2) ]
        
        
        
        pref_sum_1 = [0 for _ in range(n + 2) ]
        
        
        for i in range( n ):
            
            pref_sum_0[i + 1] = pref_sum_0[i] + grid[0][i]
            
        for i in range(n):
            
            pref_sum_1[i + 1] = pref_sum_1[i] + grid[1][i]
            
        
        min_ = float('inf') 
        
        for i in range(1, n + 1):
             
            min_ = min(min_ , max(pref_sum_0[-2] - pref_sum_0[i] , pref_sum_1[i-1]) )
            
        return(min_)
        
            
            
            
            
            
            
        
        