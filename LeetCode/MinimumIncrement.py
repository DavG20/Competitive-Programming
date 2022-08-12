class Solution(object):
    def minIncrementForUnique(self,nums):
        count =0
        nums.sort()
        for index in range(1,len(nums)):
            if nums[index]<=nums[index-1]:
                count+=(nums[index-1]-nums[index]+1)
                nums[index]=nums[index-1]+1
        
                   
        return(temp)
