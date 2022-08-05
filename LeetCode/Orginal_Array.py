class Solution(object):
    def findOriginalArray(self,Changed):
        freqNum={}
        for i in range(len(Changed)):
            if (Changed[i] in freqNum):
                freqNum[Changed[i]]+=1
            else:
                freqNum[Changed[i]]=1
        Changed.sort()
        res=[]
        for i in range(len(Changed)):
            freq=freqNum[Changed[i]]
            if freq>0 and freqNum[2*Changed[i]] :
                res.append(Changed[i])
                freqNum[Changed[i]]-=1
                twice=2*Changed[i]
                freqNum[twice]-=1
            
        return res

