class Solution(object):
    def targetIndices(self, nums, target):
        data=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        for x in range(len(nums)):
            if(target==nums[x]):
                data+=[x]
                
        return data
x=Solution()
print(x.targetIndices([1,2,5,2,3],2))