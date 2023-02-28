class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def rec(n):
            
            if n == 1:
                return True
            
            if n < 1 or n % 2 :
                
                return False
            
            return rec(n//2)
        return rec(n)
        