class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_count = Counter(p)
        res  = []
        window = {}
        have , need  = 0 , len(p_count)
        l = 0 
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0 ) + 1
            
            if window[s[r]] == p_count.get(s[r] , 0 ):
                have += 1
            elif window[s[r]] == p_count.get(s[r], 0 ) + 1:
                have -= 1
            
            
            if r - l + 1 == len(p):
                
                if have == need:
                    res.append(l)
                    
                
                
                if window[s[l]] == p_count.get(s[l], 0 ):
                    have -= 1
                
                elif window[s[l]] - 1 == p_count.get(s[l], 0 ):
                    have += 1
                
                window[s[l]] -= 1
                
                l += 1
        return res
            
            
#         l = 0 
#         p_counter = Counter(p)
#         res = []
#         window = {}
#         for r in range(len(s)):
            
#             window[s[r]] = window.get(s[r], 0 ) + 1
            
#             if r - l + 1 == len(p):
                
#                 if window == p_counter:
#                     res.append(l)
                
#                 window[s[l]] -= 1
                
#                 if window[s[l]] == 0:
#                     window.pop(s[l])
                    
#                 l += 1
#         return res
