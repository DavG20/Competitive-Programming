
class Solution(object):
    def topKFrequent(self,nums,k):
        count=Counter(nums)
        count=sorted(count.items(),kay= lambda x:x[1],reverse=True)
        res=[]
        for num in count:
            res.append(num)
        return res[:k]
             
 
