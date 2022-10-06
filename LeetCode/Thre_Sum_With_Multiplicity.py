from collections import Counter
class Solution(object):
    def threeSumMulti(self,arr,target):
        m=10**9 +7
        count=Counter(arr)
        result=0
        for i ,x in count.items():
            for j, y in count.items():
                k=target-i-j
                if k not in count:
                    continue
                if i==j and j==k: #if three numbers are same then the combination will be minimize by 6
                    result=(result+ (x*(x-1)*(x-2))//6)%(m)
                if i==j and j!=k: #if two nums are same then the combination will reduced by a factore of two
                    result=(result + (x* (x-1)//2 *count[k]))%m
                if i<j and j<k:
                    result=(result + x*y*count[k])%m
        return result %m



c=Solution()
print(c.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))