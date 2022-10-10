class Solution(object):
    def minSubArrayLen(self,target,nums):
        result=float('inf')
        count_indx=0
        sums=0
        for i in range(len(nums)):
            while count_indx<len(nums) and sums<target:
                sums+=nums[count_indx]
                count_indx+=1
            if sums>=target:
                result=min(result, count_indx)
            sums-=nums[i]
        if result==float('inf'): #so it doesn't return 'inf' when there is not sun array
            return 0
        return result