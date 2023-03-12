class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        stack = []
        
        min_ = nums[0]
        
        
        for num in nums :
            
            
            while stack and stack[-1][0] <= num :
                
                stack.pop()
                
            
            
            if stack and stack[-1][1] < num :
                
                return True
            
            
            stack.append((num , min_))
            
            
            min_ = min(min_ , num)
            
        