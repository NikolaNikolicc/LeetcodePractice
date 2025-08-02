class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        dp = [1, 2]

        i = 2
        while i < n:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp

            i += 1

        return dp[1]

        # 3
        # 2, 3
        # tmp = 2