class Solution(object):
    def subarraySum(self,nums,k):
        dic =defaultdict(int)
        sum=0
        result=0
        dic[0]=1
        for num in nums:
            sum+=num
            if sum-k in dic:
                result+=dic[sum-k]
            dic[sum]+=1
        return result