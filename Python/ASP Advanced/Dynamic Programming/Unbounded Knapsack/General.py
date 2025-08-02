class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(capacity + 1)

        for i in range(len(profit)):
            for j in range(1, capacity + 1):
                if j - weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j - weight[i]] + profit[i])

        return dp[-1]