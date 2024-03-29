class NumArray:

    def __init__(self, nums: List[int]):
        self.prefSum = [0]
        
        for i in range(len(nums)):
            
            self.prefSum.append(self.prefSum[-1] + nums[i])
            
        print(self.prefSum)
            
            
        
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefSum[right +1 ] - self.prefSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)