class Solution(object):
    def reverseParentheses(self,s):
        char_stack=[]
        # temp=""
        for i in range(len(s)): 
            if s[i]==")":
                temp=""
                while char_stack[len(char_stack)-1]!="(":
                    temp=temp+char_stack.pop()
                char_stack.pop()
                char_stack.append(temp[::-1])
                
            else:
                char_stack.append(s[i])
        return(char_stack[0][::-1])
                    
                