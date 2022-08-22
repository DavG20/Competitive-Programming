from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self,nums,k):
        result,current_sum=0
        dict=defaultdict(int)
        dict[0]=1
        for i in range(len(nums)):
            current_sum+=nums[i]
            if current_sum-k in dict:
                result+=dict[current_sum-k]
            dict[current_sum]+=1
        return result