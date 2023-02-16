class Solution(object):
    def lengthOfLongestSubstring(self,s):
        max_length=0
        Unique_list=[]
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                if s[j]in Unique_list:
                    Unique_list=[]
                    break
                else:
                    Unique_list.append(s[j])
                    if max_length<j-i+1:
                        max_length=j-i+1
        return max_length
