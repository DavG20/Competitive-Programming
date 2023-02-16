from random import randrange
import re


class Solution(object):
    def smallerNumbersThanCurrent(self,nums):
        data=[0 for i in range(len(nums))]
        for i in  range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    data[i]+=1
                elif nums[i]<nums[j]:
                    data[j]+=1
        return data
x=Solution()
print(x.smallerNumbersThanCurrent([8,1,2,2,3]))

