class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        left = 0 
        
        missed_num = 0
        
        
        while left < len(nums):
            
            if left < len(nums) and nums[left] == left :
                
                left += 1
                
            elif nums[left] == len(nums) :
            
                missed_num =  left
                
                
                left += 1
                
            else:
        
                
                nums[nums[left]] , nums[left] =  nums[left] , nums[nums[left]]
                
        if nums[missed_num] == missed_num:
            
            return len(nums)
        
        return missed_num
                
        
#         left = 0 
        
#         distnict_num = set(nums)

#         for i in range(len(nums) + 1):
            
#             if i not in distnict_num:
#                 return i
        
