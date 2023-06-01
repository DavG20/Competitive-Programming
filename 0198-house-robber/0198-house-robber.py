class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def dp(pos ,nums , memo):
            
            if pos >= len(nums):
                
                return 0
            

            if not pos in memo:
                
                cost1 = dp(pos + 2 , nums  , memo) + nums[pos]
                
                cost2 = dp(pos + 1  , nums  , memo)
                
                memo[pos] = max(cost1 , cost2)
            
            return memo[pos]
            
        memo = defaultdict(int)
        dp(0 , nums , memo)
        
        print(memo)
        return memo[0]