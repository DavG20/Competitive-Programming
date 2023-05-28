class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        
        if n == 1:
            
            return 1
        
        if n == 0:
            
            return 0
        
        arr = [0 for i in range(n + 1)]
        
        
        arr[1] = 1
        max_ = 1
        for i in range(2 , n  + 1):
            
            if i %2 == 0 :
                
                arr[i] = arr[i // 2]
                
                max_ = max(max_ , arr[i])
            else: 
                arr[i] = arr[ (i ) // 2 + 1] + arr[ i // 2]
                max_ = max(max_ , arr[i] )
                
        return max_
                
                
                