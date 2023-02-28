class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0 
    
        
        perm_count = Counter(s1)
        
        n = len(s1)
        
        for i  in range(len(s2)):
            
            
            if s2[i] in perm_count:
                perm_count[s2[i]] -= 1
                
            
            if i  >= n and s2[ i - n] in perm_count:
                perm_count[s2[i - n]] += 1
                
            
                
            if all([perm_count[i] == 0 for i in perm_count]) :
                return True
                
                
                
                
              
                    
            
            
                
                
        
        
        