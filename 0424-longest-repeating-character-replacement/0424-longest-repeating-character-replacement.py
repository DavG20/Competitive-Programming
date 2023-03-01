class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        visited_letter = defaultdict(lambda : 0)
        
        
        left = 0
        
        max_ = 0
        
        for i in range(len(s)):
            
            visited_letter[s[i]] += 1
            
            max_freq = max(visited_letter , key = visited_letter.get)
            
            
            if (i - left + 1) - visited_letter[max_freq] > k :
                
                visited_letter [s[left]]  -= 1
                
                left += 1
                
            max_ = max(max_ , i - left + 1  )
            
        return max_