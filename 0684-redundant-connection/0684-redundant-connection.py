class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a , b in edges:
            
            cycle = uf.union(a , b)
            
            if cycle:
                
                return [a , b]
        

        
class UnionFind:
    def __init__(self, n):
        
        self.Parent = {i + 1 : 1 + i for i in range(n)}
        
        
    def find(self, x):
        
        if self.Parent[x] != x:
            self.Parent[x] = self.find(self.Parent[x])
            
        return self.Parent[x]
        
    def union(self, x, y):
        
        parent_x = self.find(x)
        parent_y = self.find(y)
        # print(parent_x , parnet_y)
        
        self.Parent[parent_y] = parent_x  
        
        if parent_x == parent_y :
            return True 
        return False
        
        
        
        