class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        
        return max ((self.area(r , c, grid, seen))
             for r in range(len(grid))
             for c in range(len(grid[0])))
        
        
    
    
    def area(self,r, c, grid , seen):
        inbound = lambda x , y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        if not (inbound(r , c) and (r, c) not in seen and grid[r][c]):
            
            return 0
        
        seen.add((r,c))
        
        return (1 + self.area(r + 1, c, grid, seen) + self.area(r - 1, c, grid, seen) + self.area(r, c + 1, grid, seen) + self.area(r , c - 1, grid, seen))