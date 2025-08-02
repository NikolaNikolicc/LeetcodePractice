from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[-1] = 1

        for c in range(len(coins) - 1, -1, -1):
            for a in range(amount, -1, -1):
                if a + coins[c] < amount + 1:
                    dp[a] = dp[a] + dp[a + coins[c]]
            print(dp)
        return dp[0]

sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount, coins))