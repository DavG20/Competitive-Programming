class Solution(object):
    def getDescentPriods(self,prices):
        length=len(prices)
        if length==1:
            return 1
        arr=[1 for _ in range(length)]
        for i in range(1,length):
            if prices[i]+1==prices[i-1]:
                arr[i]+=arr[i-1]
        return sum(arr)
            