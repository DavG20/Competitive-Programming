class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
        stack = [0]
        
        
        for char in s:
            
            if char == "(":
                stack.append(0)
                
            else:
                val = stack[-1]
                
                stack.pop()
                
                stack[-1] += max(2 * val , 1) # since () is 1 and we added 0 for every ( 
                
        return stack.pop()