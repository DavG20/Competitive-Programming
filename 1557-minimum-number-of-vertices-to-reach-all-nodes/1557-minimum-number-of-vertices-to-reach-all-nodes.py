class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        Source = set(i for i in range(n))
        
        
        for a , b in edges:
            
            if Source and b in Source :
                
                Source.remove(b)
                
        return list(Source)