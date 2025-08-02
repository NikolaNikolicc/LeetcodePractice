# abc
# adef

# ad ab ef c

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i1 in range(len(s1), -1, -1):
            for i2 in range(len(s2), -1, -1):

                if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dp[i1 + 1][i2]:
                    dp[i1][i2] = True
                
                if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dp[i1][i2 + 1]:
                    dp[i1][i2] = True   

            print(dp[i1])                 

        return dp[0][0]
                
sol = Solution()
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
print(sol.isInterleave(s1, s2, s3))