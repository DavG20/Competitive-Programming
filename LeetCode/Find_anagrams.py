class Solution(object):
    def findAnagrams(self,s ,p):
        
        p_length,s_length=len(p),len(s)
        s_list,p_list=list(s),list(p)
        p_list.sort()
        result=[]
        for i in range(s_length-p_length+1):
            temp=s_list[i:i+p_length]
            temp.sort()
            if temp==p_list:
                result.append(i)
            else:
                continue
        return(result)


c=Solution()
c.findAnagrams("abab","ab")