class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        start_sum = 0
        
        end_sum = 0
        
        if len(nums) <= 4:
            
            return 0
        
        return min(nums[-3] - nums[1] , nums[-2] - nums[2] , nums[-1] - nums[3] , nums[-4] - nums[0])
        
        
        
        
            
            
            