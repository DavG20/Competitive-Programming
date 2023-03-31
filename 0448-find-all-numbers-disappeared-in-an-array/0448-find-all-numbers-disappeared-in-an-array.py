class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        missed_num = []
        
        left = 0
        
        while left < len(nums) :
            
            if nums[nums[left] - 1] != nums[left] :
                
                nums[nums[left] - 1] , nums[left] = nums[left] , nums[nums[left] - 1]
                
            else:
                
                left += 1
                
        for i in range(len(nums)):
            
            if i + 1 != nums[i] :
                missed_num.append(i + 1)
                
        return missed_num
            
            