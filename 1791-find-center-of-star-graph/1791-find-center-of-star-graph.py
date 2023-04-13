class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        
        center = defaultdict(int)
        
        for a , b in edges:
            
            center[a] += 1
            
            center[b] += 1
        
        for a , b in edges:
            if center[a] == len(edges):
                return a
            if center[b] == len(edges):
                return b
        
        return 0
            
            
        
        
            