class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.prefSum = [self.nums[0]]
        for i in range (1,len(self.nums)):
            self.prefSum.append(self.nums[i] + self.prefSum[-1]) 
    def sumRange(self, left: int, right: int) -> int:
        
        
        if left ==0:
            return self.prefSum[right]
        else:
            return self.prefSum[right] - self.prefSum[left-1]
        
        
        
#         sum_ = 0
        
#         for i in range(right - left + 1):
            
#             sum_ += self.nums[i + left]
#         return sum_
            
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)