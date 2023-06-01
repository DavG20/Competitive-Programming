class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return max(nums)
        
        # nums.append(0)
        def dp_one( pos ,nums , memo):
            
            if pos >= len(nums) :
                
                return 0
            if not pos in memo:
                
                cost1 = dp_one(pos + 2 , nums , memo) + nums[pos]
                
                cost2 = dp_one(pos + 1 , nums ,memo)
                
                memo[pos] = max(cost1 , cost2)
                
            return memo[pos]
        
        def dp_zero( pos ,nums , memo):
            
            if pos >= len(nums) - 1:
                
                return 0
            if not pos in memo:
                
                cost1 = dp_zero(pos + 2 , nums , memo) + nums[pos]
                
                cost2 = dp_zero(pos + 1 , nums ,memo)
                
                memo[pos] = max(cost1 , cost2)
                
            return memo[pos]
    
        memo_zero = defaultdict(int)
        memo_one = defaultdict(int)
        
        cost_zero = dp_zero(0 , nums , memo_zero)
        
        cost_one = dp_one(1 , nums , memo_one)
        # print(memo_one , memo_zero)
        return max(cost_one , cost_zero)
        

        
        
        