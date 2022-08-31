class Solution(object):
    def countVowels(self,word):
        count_Val=[0]* (len(word)+1)
        
        for i ,char in enumerate(word):
            count_Val[i+1]=count_Val[i]+((char in "aeiou") *(i+1))
        return sum(count_Val)