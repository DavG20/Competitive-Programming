class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        
        
        
        if n == 1:
            
            return "0"
        
        num_col = 2**n - 1
        
        mid = num_col // 2
        
        if k <= mid :
            
            return self.findKthBit(n - 1, k )
        
        elif k == mid + 1:
            
            return "1"
        else:
            
            k = num_col - k + 1
            
            s = self.findKthBit(n - 1, k )
            
            return "1" if s == "0" else "0"
            
            
            
            
    