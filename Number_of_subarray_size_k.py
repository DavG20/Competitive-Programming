class Solution(object):
    def numOfSubarrays(self,arr,k,threshold):
        # count=0
        # for i in range(len(arr)-k+1):
        #     temp=arr[i:k+i]
        #     if sum(temp)/k>=threshold:
        #         count+=1
        # return count
        #the above code didn't pass the time limit
        res=0
        count=0
        for i in range((len(arr))):
            if i<k-1:
                count+=arr[i]
            elif i==k-1:
                count+=arr[i]
                if count/k>=threshold:
                    res+=1
            else:
                count+=arr[i]
                count-=arr[i-k]
                if count/k>=threshold:
                    res+=1
        return(res)
c=Solution()
c.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)