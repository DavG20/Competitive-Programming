class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(point):
            
            if point == (m - 1, n - 1):
                return 1
            row , col = point 
            
            ways = 0
            
            if row + 1 < m :
                
                ways += dp((row + 1 , col))
            if col + 1 < n :
                
                ways += dp((row  , col + 1))
                
            return ways 
                
        return dp((0 , 0))