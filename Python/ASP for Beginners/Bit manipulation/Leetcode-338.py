from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]

        offset = 1
        for i in range(1, n + 1):
            if i == offset << 2:
                offset <<= 2

            dp[i] = dp[i - offset] + 1

        return dp

    def countBitsDP(self, n):
        dp = [0] * (n + 1)

        offset = 1
        for i in range(1, n + 1):
            if i == (offset << 1):
                offset <<= 1

            dp[i] = dp[i - offset] + 1

        return dp

    def countBitsOptimal(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


sol = Solution()
print(sol.countBitsDP(5))