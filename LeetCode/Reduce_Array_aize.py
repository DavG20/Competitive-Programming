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
            count+=1
            if(size_set>=len(arr)/2):
                break
        return count
                
                
            
                
            
        print("this is store",store,"this is the count value",count)
c=Solution()
print(c.minSetSize([7,7]))