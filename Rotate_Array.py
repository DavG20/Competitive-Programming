class Solution(object):
    def rotate(self,nums,k):
        length=len(nums)
        k=k%length
        nums[:]=(nums[length-k:]+nums[:length-k])
c=Solution()
c.rotate([1,2,3,4,5,6,7]
,3)