class Solution:
    def findTheWinner(self, n, k):
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
                
c=Solution()
c.findTheWinner(8, 7)