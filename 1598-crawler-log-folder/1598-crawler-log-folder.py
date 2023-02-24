class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        
        for log in logs:
            
            dirc = log.split("/")
            
            if dirc[0] == "..":
                if stack:
                    stack.pop()
            elif dirc[0] == ".":
                continue
            else:
                stack.append(log)
        return len(stack)
                
            
            
                
        