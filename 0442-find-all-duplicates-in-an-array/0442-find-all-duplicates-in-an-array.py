class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        left = 0
        
        
        while left < len(nums) :
            
            if nums[nums[left] - 1] != nums[left] :
                
                nums[nums[left] - 1] , nums[left] = nums[left] , nums[nums[left] - 1]
            else:
                left += 1
                
        duplicated_num = []
        
        for i in range(len(nums)) :
            
            if nums[i] != i + 1 :
                
                duplicated_num.append(nums[i])
                
        return duplicated_num
        