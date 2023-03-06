class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        
        stack_mo = []
        
        dp = [0] * len(arr)
        
        sumOfMin = 0
        
        for i in range(len(arr)):
            
            while stack_mo and arr[stack_mo[-1]] >= arr[i] :
                
                stack_mo.pop()
                
            if stack_mo:
                prevSmaller = stack_mo[-1]
                
                dp[i] = dp[prevSmaller] + (i - prevSmaller)  * arr[i]
            else:
                
                dp[i]  = (i + 1) * arr[i]
            stack_mo.append(i)
                
        return sum(dp) % (10 ** 9 + 7)
            