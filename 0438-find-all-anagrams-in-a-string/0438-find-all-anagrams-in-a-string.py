class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_count = Counter(p)
        
        windows = {}
        
        arr = []
        
        left = 0
        
        for right in range(len(s)):
            
            windows[s[right]] = windows.get(s[right],0) + 1
            
            if right - left + 1 == len(p):
                
                if p_count == windows:
                    
                    arr.append(left)
                
                windows[s[left]] -= 1
                
                if windows[s[left]] == 0:
                    windows.pop(s[left])
                left += 1
                
        return arr
                