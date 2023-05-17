

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)
            
        
        return uf.find(source) == uf.find(destination)
    
class UnionFind:
    def __init__(self, n):
        self.Parent = {i : i for i in range(n)}
        
        
    def find(self, x):
        
        if self.Parent[x] != x:
            self.Parent[x] = self.find(self.Parent[x])
            
        return self.Parent[x]
        
    def union(self, x, y):
        
        parent_x = self.find(x)
        parnet_y = self.find(y)
        # print(parent_x , parnet_y)
        self.Parent[parnet_y] = parent_x
        
        
        
        
        
        
        
            
            