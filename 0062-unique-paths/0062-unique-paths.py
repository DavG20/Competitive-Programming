class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # @cache
        memo = defaultdict(int)
        def dp(point , memo):
            
            if point == (m - 1, n - 1):
                return 1
            row , col = point 
            
            ways = 0
            
            if row + 1 < m :
                if  (row + 1 , col) in memo:
                    ways += memo[(row + 1 , col)]
                else:
                    memo[(row + 1 , col)] = dp((row + 1 , col) , memo)
                    ways += memo[(row + 1 , col)]
            if col + 1 < n :
                
                if  (row  , col + 1) in memo:
                    ways += memo[(row  , col + 1)]
                else:
                    memo[(row  , col + 1)] = dp((row  , col + 1) , memo)
                    ways += memo[(row  , col + 1)]
                
            return ways 
                
        return dp((0 , 0) , memo)