class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        last = 1 & (n >> 0)
        
        n >>= 1
        while n :
            
            
            print(last , n)
            if (last) & ((n >> 0) & 1) == 0 :
                
                if ((n >> 0) & 1) == 0 and last == 0:
                    return False
                last = (n >> 0)  & 1
                
            else:
                return False
            n >>= 1
        return True
            