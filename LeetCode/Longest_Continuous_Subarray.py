class Solution:
    def longestSubarray(self, nums, limit): 
        maxlen=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                tmp=nums[i:j]
                if max(tmp)-min(tmp)<=limit:
                    if len(tmp)>lenmax:
                        lenmax=len(tmp)
        return maxlen

