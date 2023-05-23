class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind()
        
        for equation in equations:
            if equation[1] + equation[2] == "==" :
                uf.Union(equation[0], equation[3])
                
        for equation in equations:
            
            if equation[1] + equation[2] == "!=" and uf.isConnected(equation[0], equation[3]):
                # if uf.isConnected(equation[0], equation[3]):
                
                return False
        
            
        return True
                
            
        
            
            

        
        
        
        
        
        
        
class UnionFind:
    
    def __init__(self ):
        
        self.Parent = { chr(ord("a") + i ) : chr(ord("a") + i ) for i in range(26) }
        
        
    def find(self , x):
        
        if self.Parent[x] != x:
            
            self.Parent[x] = self.find(self.Parent[x])
            
        return self.Parent[x]
        
    def Union(self , x, y):
        
        parentx = self.find(x)
        
        parenty = self.find(y)
        
        self.Parent[parenty] = parentx
        
    def isConnected(self , a , b):
        
        return self.find(a) == self.find(b)