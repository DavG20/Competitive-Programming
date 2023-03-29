class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = []
        for i in range(n + 1):
            
            count = 0
            
            for bit_digt in range(64):
                
                if i & (1 << bit_digt):
                    
                    count += 1
                
            arr.append(count)
            
        return arr
        
            