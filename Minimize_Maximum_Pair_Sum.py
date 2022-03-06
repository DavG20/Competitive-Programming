from dataclasses import dataclass


class Solution:
    def minPairSum(self,nums):
        data=[]
        nums.sort()
        for i in range(int(len(nums)/2)):
            data+=[nums[i]+nums[len(nums)-i-1]]
        return max(data)    
