class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        
        hold, sell = [0] * n , [0] * n
        
        hold[0] = -prices[0]
        
        for i in range(1, n):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i] - fee)
        
        return sell[-1]