class Solution(object):
    def maxVowels(self,s,k):
        max_Vowel,result=0,0
        Vowel=["a","e","i","o","u"]
        for i in range(len(s)):
            if i>=k:
                if s[i-k] in Vowel:
                    result-=1
            if s[i] in Vowel:
                result+=1
            max_Vowel=max(max_Vowel,result)
            if max_Vowel==k:
                return max_Vowel
        return max_Vowel

