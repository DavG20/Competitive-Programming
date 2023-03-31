class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        print((x & 1) ^ (y & 1))
        count_bit_diff = (x & 1) ^ (y & 1)
        
        while x or y :
            
            count_bit_diff +=( (x >> 1) & 1) ^ ( (y >> 1) & 1) 
            
            x >>= 1
            y >>= 1
            
        return count_bit_diff 
            
            