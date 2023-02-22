class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0 
        p_counter = Counter(p)
        res = []
        window = {}
        for r in range(len(s)):
            
            window[s[r]] = window.get(s[r], 0 ) + 1
            
            if r - l + 1 == len(p):
                
                if window == p_counter:
                    res.append(l)
                
                window[s[l]] -= 1
                
                if window[s[l]] == 0:
                    window.pop(s[l])
                    
                l += 1
        return res
