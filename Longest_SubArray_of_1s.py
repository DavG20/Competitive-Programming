class Solution(object):
    def longestSubarray(self,nums):
        # res,max_res=0,0
        # count=0
        # for j in range(len(nums)):
        #     res=0
        #     count=0
        #     for i in range(j,len(nums)):
        #         if nums[i]==0 and count==1:
        #             count=0
        #             max_res=max(max_res,res)
        #             res=0
        #             break
        #         if nums[i]==1 and count==0:
        #             res+=1
        #         if nums[i]==0 and count==0:
        #             res+=1
        #             count+=1
        #     max_res=max(max_res, res)
        # return -1
#but the above code don't pass the time limit
        i=0
        count_zero=1
        result=0
        for j in range(len(nums)):
            if nums[j]==0:
                count_zero-=1
            while i<len(nums) and k<0:
                if nums[j]==0:
                    k-=1
                i+=1
            result=max(result,j-i+1)
        return result-1
            



