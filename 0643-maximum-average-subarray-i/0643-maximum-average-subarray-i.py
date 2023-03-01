class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        
        sum_ , l = 0  , 0
        
        max_ = - float('inf')
        
        for r in range(len(nums)):
            
            sum_ += nums[r]
            
            if r - l + 1 == k :
                max_ = max(max_ , sum_/k)
                
                sum_ -= nums[l]
                
                l += 1
        return max_

                
                
                
        