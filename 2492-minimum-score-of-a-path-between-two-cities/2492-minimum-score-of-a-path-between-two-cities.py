class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        
        
        
        for a , b , distance in reversed(roads):
            
            uf.Union(a - 1 , b  - 1, distance)
        
        ans = float("inf")
        
        for a , _ , distance in roads:
            
            if uf.isConnected(a - 1, n - 1):
                ans = min(ans , distance)
            
            
            
            
        
        return ans 
    
    


class UnionFind :
    
    def __init__(self, n):
        
        self.Parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
        
        
    def find(self , x):
        
        if self.Parent[x] != x :
            
            self.Parent[x] = self.find(self.Parent[x])
        
        return self.Parent[x]
    
    
    def Union(self , x , y , distance):
        
        parentx = self.find(x)
        
        parenty = self.find(y)
        
        
        if parentx == parenty:
            
            return 
        
        if self.rank[parentx] == self.rank[parenty]:
            
            self.rank[parentx] += 1
            
        if self.rank[parentx] > self.rank[parenty]:
            
            self.Parent[parenty] = parentx
            
        if self.rank[parentx] < self.rank[parenty]:
            
            self.Parent[parentx] = parenty
        
        
        
        
    def isConnected(self , x , y):
        
        return self.find(x) == self.find(y)
        
        
        
        
    