class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maximize profit
        # buy cheap, sell high

        buy = 0
        maxProfit = 0
        for p in range(1, len(prices)):
            if prices[buy] > prices[p]:
                buy = p

            maxProfit = max(maxProfit, prices[p] - prices[buy])
        return maxProfit
