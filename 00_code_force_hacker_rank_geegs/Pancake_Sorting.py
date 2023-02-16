from dataclasses import dataclass


class Solution:
    def pancakesort(self,arr):
        data=[]
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                for x in range(j+1,len(arr)-1):
                    if arr[j]>arr[x]:
                        data+=[x+1]
                        print(arr[::-x],"the reverse")
                        arr=arr[::-x]
                        
                        # arr[j],arr[x]=arr[x],arr[j]
                    # print(data,'this is the arr',arr)
            print(arr)
        

c=Solution()
c.pancakesort([3,2,4,1])