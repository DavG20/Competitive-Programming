

class Solution(object):
    def largestNumber(self,nums):
        res=[]
        result=""
        for i in range(len(nums)):
            s=[int(x)for x in str(nums[i])]
            for i in range(len(s)):
                res.append(s[i])
        res.sort(reverse=True)
       
        for i in range(len(res)):
            result+=str(res[i])
        return result
            
                
c=Solution()
print(c.largestNumber([3,30,34,5,9]))