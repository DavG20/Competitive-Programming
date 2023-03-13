class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        ans = [-1 for _ in range(len(nums))]

        
        stack = []
        
        
        for indx in range(2 * len(nums)):
            
            while stack and nums[stack[-1]] < nums[indx % n]:
                
                ans[stack[-1]] = nums[indx % n]
                
                stack.pop()
                
                
        
           
                
            stack.append(indx % n)
            
        return ans
            
            
        
            
            