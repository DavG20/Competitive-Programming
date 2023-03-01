class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sum_=0
        count=0
        min_=sys.maxsize
        for i in range(len(nums)):
            while count<len(nums) and sum_<target:
                sum_+=nums[count]
                count+=1
            if sum_>=target:
                min_=min(min_,count-i)
            sum_-=nums[i]
        if min_==sys.maxsize:
            return 0
        return min_
        