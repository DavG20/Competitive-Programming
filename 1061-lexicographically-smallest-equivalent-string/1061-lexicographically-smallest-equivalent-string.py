class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        
        uf = UnionFind(len(s1))
        
        
        
        
        
        
        for i in range(len(s1)):
            
            uf.Union(s1[i] , s2[i] )
            
            
        ans = ""
        
        for char in baseStr:
            
            ans += uf.find(char)
            
            
        
        
        
        
        return ans
        
        

        
class UnionFind :
    
    def __init__(self, n):
        
        self.Parent = { chr(ord("a") + i ) : chr(ord("a") + i ) for i in range(26) }
        
        
        

        
    def find(self , x):
        
        if self.Parent[x] != x :
            
            self.Parent[x] = self.find(self.Parent[x])
        
        return self.Parent[x]
    
    
    def Union(self , x , y ):
        
        parentx = self.find(x)
        
        parenty = self.find(y)
        
        
        
        self.Parent[parentx] = min( parentx, parenty)
        self.Parent[parenty] = min( parenty, parentx)
        
        
        
        
        
  