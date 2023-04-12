class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        return self.GCD(min(nums) , max(nums))
        
    
    def GCD(self ,a , b):
        if b == 0 :
            
            return a
        
        return self.GCD(b , a % b)
        