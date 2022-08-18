class Solution(object):
    def lengthOfLongestSubstring(self,s):
        counter=0
        result=""
        stack=[]
        for char in s:
            if char not in result:
                result=result+char 
                counter+=1
            else:
                stack.append(counter)
                counter=0
                result=""
            stack.append(counter)
        return max(stack)
