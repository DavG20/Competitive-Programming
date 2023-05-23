class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        uf = UnionFind(len(stones))
        
        
        for i in range(len(stones)):
            
            for j in range(i + 1, len(stones) ):
                
                if stones[i][0] == stones[j][0] or  stones[i][1] == stones[j][1]:
                    
                    uf.Union(i , j )
                    
        
        
        
        count = 0
        for i in range(len(stones)):
            
            if uf.find(i) != i :
                count += 1
                
        return count
                
        
        
        
    
    

class UnionFind :
    
    def __init__(self, n):
        
        self.Parent = [i for i in range(n)]
        
        
    def find(self , x):
        
        if self.Parent[x] != x :
            
            self.Parent[x] = self.find(self.Parent[x])
        
        return self.Parent[x]
    
    
    def Union(self , x , y ):
        
        parentx = self.find(x)
        
        parenty = self.find(y)
        
        self.Parent[parenty] = parentx
        
    
        
        

            
            
        
        
        
        
   
        
        