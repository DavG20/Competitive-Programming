class Solution(object):
    def maxFrequency(self,nums,k):
        x=k
        res=[]
        temp=0
        while x>0:
            for i in range(len(nums)-1):
                print(sum(res),"this is the sum of res")
                for j in range(i+1,len(nums)):
                    if temp<nums[j]-nums[i] and (sum(res)+(nums[j]-nums[i]))<k:
                        print(j,"this is j")
                        temp=nums[j]-nums[i]
                        x-=nums[j]-nums[i]
                    
                        
                        
                x-=temp
                print(x)
                res.append(temp)
                            
                
            print(res)
    def sum(arr):
        sum=0
        for i in arr:
            sum+=i
        return sum 
c=Solution()
c.maxFrequency([2,2,3,9],5)
                    
                