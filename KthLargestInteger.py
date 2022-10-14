class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums.sort(key=lambda x:int(x))
        return nums[len(nums)-k]
