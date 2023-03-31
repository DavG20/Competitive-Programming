class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        left = 0 
        
        while left < len(nums) :
            
            if nums[nums[left] - 1] != nums[left] :
                
                nums[nums[left] - 1] , nums[left] = nums[left] ,nums[nums[left] - 1] 

            else:
                left += 1
        print(nums)
        
        for i in range(len(nums)) :
            
            if nums[i] != i + 1:
                
                return nums[i]
                