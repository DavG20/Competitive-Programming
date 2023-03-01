class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        
        for char in tokens:
            
            
                
            if char == "+":
                num2 = stack.pop()
                
                stack.append(stack.pop() + num2)
            elif char == "*":
                num2 = stack.pop()
                
                stack.append(stack.pop() * num2)
            elif char == "/":
                num2 = stack.pop()
                
                num1 =stack.pop()
                
                q = num1 / num2 
                
                stack.append(int(str(q).split(".")[0]))
                
                
                
            elif char == "-":
                num2 = stack.pop()
                
                stack.append(stack.pop() - num2)
            else:
                
                stack.append(int(char))
                
        return stack[-1]
            
            