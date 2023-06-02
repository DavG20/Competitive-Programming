class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(row , col):
            
            if row == len(triangle):
                
                return 0
            
            path1 = dp(row + 1 , col) + triangle[row][col]
            path2 = dp(row + 1 , col + 1) + triangle[row][col]
            
            return min(path1 , path2)
            
            
        return dp(0 , 0)                
        