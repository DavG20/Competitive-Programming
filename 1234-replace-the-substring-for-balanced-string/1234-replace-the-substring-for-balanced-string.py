class Solution:
    def balancedString(self, s: str) -> int:
        
        
        left = 0
        
        n = len(s)
        
        ans  = len(s)
        
        
        c = Counter(s)
        
        
        for right in range(n):

            c[s[right]] -= 1
        
            
            while left < n and  c["R"] <= n//4 and c["Q"] <= n//4 and c["E"] <= n//4 and c["W"] <= n//4:
                
                ans = min(ans , right - left + 1)
                
                c [s[left]] += 1
                
                left += 1
                
                
                
        return ans
                
        
        