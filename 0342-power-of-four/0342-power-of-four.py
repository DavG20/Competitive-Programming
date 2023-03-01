class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
       
        def rec(num):
            
            if num == 1:
                return True
            if num < 1 or num%4 :
                
                return False 
            return rec(num//4)
            
        return rec(n)
        
        
        
        
        