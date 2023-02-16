class Solution(object):
    def isValid(self,s):
        stack =[]
        for chars in s:
            if chars=="(" or chars=="{" or chars=="[":
                stack.append(chars) 
            elif chars==")" and stack!=[] and stack[len(stack)-1]=="(":
                print("in (")
                stack.pop()
            elif chars=="}" and stack!=[] and stack[len(stack)-1]=="{":
                print("in {")
                stack.pop()
            elif chars=="]" and stack!=[] and stack[len(stack)-1]=="[":
                print("in [")
                stack.pop()
            else :
                print("this",stack)
                return False
        print(stack)
        return stack==[]
