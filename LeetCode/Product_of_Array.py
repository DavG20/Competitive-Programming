class Solution(object):
    def productExceptSelf(self,nums):
        start,end,n=1,1,len(nums)
        result=[1]*n
        for i in range(n):
            result[i]*=start
            start*=nums[i]
            result[~i]*=end
            end*=nums[~i]
        return result