class Solution:
    def findComplement(self, num: int) -> int:
        
        shift_num = 0
        
        count = 0
        
        while num :
            if 1 & (num) == 0:
                shift_num += 2 ** count
                
            num >>= 1
            count += 1
        return shift_num
                
                