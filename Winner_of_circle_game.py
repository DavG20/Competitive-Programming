class Solution(object):
    def findTheWinner(self,n,k):
        ans=0
        for i in range(1,n):
            ans=(ans+k)%i
        return ans +1
    
            
    