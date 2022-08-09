


class Solution(object):
    def topKFrequent(self,nums,k):
        Freq_Dic={}
        Output_Store=[]
        
        for value in nums:
            if value  in Freq_Dic:
                Freq_Dic[value]+=1
            else:
                Freq_Dic[value]=1
        final_Dic=sorted(Freq_Dic.items(),key=lambda x: x[1], reverse=True)  
        for i in range(k):
            Output_Store.append(final_Dic[i][0])  
        Output_Store.sort()
        return(Output_Store)   
             
 