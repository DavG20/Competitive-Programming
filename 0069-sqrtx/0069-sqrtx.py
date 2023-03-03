class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        
        end = x//2
        
        last = x
        
        while start <= end:
            
            mid = start + ( end - start) // 2
            
            if mid ** 2 > x :
                
                end = mid -1
                
            elif mid ** 2 < x :
                last = mid
                start = mid + 1
                
                
            else:
                return mid
            
        return last
            
            
            
            
            
        
        
        