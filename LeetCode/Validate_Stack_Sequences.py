class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        i = 0 
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack
c=Solution()
print(c.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))
                    
                    
                    