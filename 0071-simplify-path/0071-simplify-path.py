class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        
        path = path.split("/")
        
        
        
        print(path)
        
        
        for char in path:
            
            if char.isalpha():
                stack.append(char)
            elif stack and char == "..":
                stack.pop()
            elif char != "." and char != "" and char != "..":
                stack.append(char)
        
        return "/" + "/".join(stack)
            
        