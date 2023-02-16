class Solution(object):
    def nextPermutation(self,nums):
       n=len(nums)
       indx=n-2
       while indx>=0:
        if nums[indx]>=nums[indx+1]:
            indx-=1
        else:
            for j in range(n-1,indx,-1):
                if nums[j]>nums[indx]:
                    nums[indx],nums[j]=nums[j],nums[indx]
                    nums[indx+1:]=sorted(nums[indx+1:])
                    return nums
        nums.reverse()
        return nums # for  testing  for leetcode just modify nums in place
          
