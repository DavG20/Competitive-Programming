class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        pref_sum = [0]
        
        Counter = defaultdict(int)
        
        
        for num in nums:
            
            pref_sum.append(pref_sum[-1] + num)
        
        
        ans = 0
        
        
        for pref  in pref_sum :
            
            ans += Counter[pref]
            
            Counter[pref + goal] += 1
        return ans
            
            
        
        