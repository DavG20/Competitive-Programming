class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        n = len(nums)
        
        prefSum_range =  [ 0 for _ in range(n)]
        
        
        
        # lets get the range for all of the request
        
        for request in requests:
            
            
            if request[1] + 1 < n:
                prefSum_range[ request[1] + 1] -= 1
                
            prefSum_range[request[0]] += 1
            
            
        for i in range(1 , n):
            
            prefSum_range[i] = prefSum_range[i-1] + prefSum_range[i]
            
      
        prefSum_range.sort()
        
        nums.sort()
        
        
        
        total_sum = 0
        
        
        for i in range(n):
            
            total_sum += nums[i] * prefSum_range[i]
            
        return total_sum % (10**9 + 7)
        
        
        
            
            
        
        
        
        