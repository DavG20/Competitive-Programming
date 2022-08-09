class Solution(object):
    def evalRPN(self,tokens):
        stack=[]
        tempo=0
        for value in tokens:
            if value =="+":
                temp=int(stack.pop()) 
                stack.append(int(stack.pop())+temp)
            elif value=="/" :
                temp=int(stack.pop()) 
                stack.append(int(stack.pop())/temp)
            elif value=="*" :
                temp= int(stack.pop()) 
                stack.append(int(stack.pop())*temp)
            elif value=="-":
                temp= int(stack.pop())
                stack.append(int(stack.pop())-temp)
            else:
                stack.append(value)
       
        return stack[0]
