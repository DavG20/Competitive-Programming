class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        dict_letter = {}
        
        visited = set()
        
        stack = []
        
        
        
        for i in range(len(s)):
            
            dict_letter[s[i]] = i
            
       
        for i in range(len(s)):
            
            if s[i] not in visited:
                
                while stack and stack[-1] > s[i] and dict_letter[stack[-1]] > i :
                    #pop fron both 
                    visited.remove(stack.pop())
                    
                visited.add(s[i])
                
                stack.append(s[i])
                
        return "".join(stack)
                
                
                
            
            