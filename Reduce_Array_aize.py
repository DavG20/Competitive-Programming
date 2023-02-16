class Solution(object):
    def minSetSize(self,arr):
        store={}
        count=0
        size_set=0
        for i in arr:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
        for i in store:
            size_set+=store[i]
            if(size_set==len(arr)/2):
                break
            elif(size_set>len(arr)/2):
                break
            else:
                count+=1
            
                
        return count
                
                
            
                
            
        print("this is store",store,"this is the count value",count)
c=Solution()
print(c.minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))