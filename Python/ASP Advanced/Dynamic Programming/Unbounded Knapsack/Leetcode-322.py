from typing import List

class Solution(object):
    def coinChangeRecursive(self, coins, amount):
        def dfs(i, currSum):
            if i == len(coins) or currSum > amount:
                return float("inf")

            if currSum == amount:
                return 0

            return min(1 + dfs(i, currSum + coins[i]), dfs(i + 1, currSum))

        ret = dfs(0, 0)
        return ret if ret != float("inf") else -1

    def coinChangeMemoization(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i, currSum):
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            if i == len(coins) or currSum > amount:
                return float("inf")

            if currSum == amount:
                return 0

            dp[(i, currSum)] = min(1 + dfs(i, currSum + coins[i]), dfs(i + 1, currSum))
            return dp[(i, currSum)]

        ret = dfs(0, 0)
        return ret if ret != float("inf") else -1

    def coinChangeMemoryOpt(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(1, amount + 1):
                if a == coin:
                    dp[a] = 1

                if a - coin >= 0 and dp[a - coin] != float("inf"):
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                
        return dp[-1] if dp[-1] != float("inf") else -1

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")]*(amount + 1)
        dp[0] = 0
        for a in range(amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a - coin] + 1, dp[a])

            print(dp)

        return dp[amount] if dp[amount] != float("inf") else -1
                

sol = Solution()
coins = [2, 5]
amount = 12
print(sol.coinChange(coins, amount))