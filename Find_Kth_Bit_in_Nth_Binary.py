class Solution(object):
    def findKthBit(self,n, k):
        if k==1:
            return str(0)
        else:
            arr=[0]
            arr2=[1]
            while k>len(arr):
                tempLast=arr[:]
                temp2Last=arr2[:]
                arr=tempLast+[1]+temp2Last
                arr2=tempLast+[0]+temp2Last
            return str(arr[k-1])
            
        
c=Solution()
print(c.findKthBit(3,2))