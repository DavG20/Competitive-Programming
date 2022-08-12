class Solution(object):
    def calculate(self, s):
        stack=[]
        temp=""
        for i in s: 
            if temp=="*":
                stack.pop()
                stack.append(int(stack.pop())*int(i))
            elif temp=="/":
                stack.pop()
                stack.append(int(stack.pop())/int(i))
            else:
                stack.append(i)
            temp=stack[len(stack)-1]
        if len(stack)>1:
            temp=""
            while len(stack)>1:
                if stack[len(stack)-1]=="+":
                    stack.pop()
                    stack.append(int(temp)+int(stack.pop()))
                elif stack[len(stack)-1]=="-":
                    stack.pop()
                    stack.append(int(temp)-int(stack.pop()))
                temp=stack.pop() 
            return temp            
        else:
            return stack[0]
         