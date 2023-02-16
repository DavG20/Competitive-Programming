from random import randrange
from typing import Counter


class Solution(object):
    def minSetSize(self, arr):
        store=[]
        freq=Counter(arr)
        # print((freq))
        for i in freq:
            # store+=[freq[i]]
        for i in range(len(store)):
            for j in range(i+1,len(store)):
                count=store[i]+store[j]
                if(store[i]+store[j])==int(len(arr)/2):
                    print(store[i],store[j])

        print(store)

             


        
            
        
c=Solution()
c.minSetSize([3,3,3,3,5,5,5,2,2,7])