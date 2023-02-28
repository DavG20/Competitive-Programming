class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        result = current_sum = 0
        
        dic = defaultdict(int)
        
        dic[0] = 1
        
        for i in range(len(nums)):
            
            current_sum += nums[i]%2
            
            if current_sum-k in dic:
                
                result += dic[current_sum-k]
                
            dic[current_sum] += 1
            
        return result 