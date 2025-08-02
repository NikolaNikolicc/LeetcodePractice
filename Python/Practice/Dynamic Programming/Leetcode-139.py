class Solution(object):
    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    print('uslo')
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        print(dp)
        return dp[0]

sol = Solution()
s="neetcode"
wordDict=["neet","code"]
print(sol.wordBreak(s, wordDict))