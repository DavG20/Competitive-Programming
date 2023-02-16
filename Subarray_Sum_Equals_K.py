from collections import defaultdict
class Solution(object):
    def subarraySum(self,nums,k):
        dic=defaultdict(int)
        result=0
        sum=0
        dic[0]=1
        for num in nums:
            sum+=num
            if sum-k in dic:
                result+=dic[sum-k]
            dic[sum]+=1
        return result
