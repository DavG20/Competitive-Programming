class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        
        
        
        for a , b , distance in reversed(roads):
            
            uf.Union(a - 1 , b  - 1, distance)
        
        
        print(uf.minEdge)
        
            
            
            
            
        
        return uf.getAnswer(n - 1) 
    
    


class UnionFind :
    
    def __init__(self, n):
        
        self.Parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
        self.minEdge = [inf for _ in range(n)]
        
        
        
    def find(self , x):
        
        if self.Parent[x] != x :
            
            self.Parent[x] = self.find(self.Parent[x])
        
        return self.Parent[x]
    
    
    def Union(self , x , y , distance):
        
        parentx = self.find(x)
        
        parenty = self.find(y)
        
        
        if parentx == parenty:
            
            self.minEdge[parentx] = min(self.minEdge[parentx] , self.minEdge[parenty],distance)
            
            return 
        
        if self.rank[parentx] == self.rank[parenty]:
            
            # self.minEdge[parentx] = min(self.minEdge[parenty] , distance)
            
            self.rank[parentx] += 1
            
        if self.rank[parentx] > self.rank[parenty]:
            
            self.minEdge[parentx] = min(self.minEdge[parenty] ,self.minEdge[parentx] , distance)
            
            self.Parent[parenty] = parentx
            
        if self.rank[parentx] < self.rank[parenty]:
            
            self.minEdge[parenty] = min(self.minEdge[parenty] ,self.minEdge[parentx] , distance)
            
            self.Parent[parentx] = parenty
        
        
        
        
    def isConnected(self , x , y):
        
        return self.find(x) == self.find(y)
    
    def getAnswer(self , n):
        
        return self.minEdge[self.find(n)]
        
        
        
    