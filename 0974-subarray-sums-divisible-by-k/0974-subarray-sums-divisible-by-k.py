class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        # use dict for storing the remainder in every iteration
        
        remainder_freq = defaultdict(lambda : 0)
        
        
        remainder_freq[0] = 1
        
        prefSum = 0
        
        answer = 0
        
        
        for num in nums:
            
            prefSum += num
            
            remainder = prefSum % k
            
            answer += remainder_freq[remainder]
            
            remainder_freq [remainder] += 1
        return answer
            
            
        
        
        
        