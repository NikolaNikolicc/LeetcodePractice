class Solution:
    def formStr(self, s: str, i: int, k: int)->str:
        i1 = str((int(s[i]) + k) % 10)
        i2 = str((int(s[i + 1]) + k) % 10)
        return s[:i] + i1 + i2 + s[i + 2:]
    
    def transform(self, s: str, t: str, k: int) -> int:
        dp = {}    

        visited = set()
        def dfs(num):
            if num in dp:
                return dp[num]

            if num == t:
                return 0

            if num in visited:
                return float("inf")

            # finding loops
            visited.add(num)

            minTransform = float("inf")
            for i in range(len(s) - 1):
                if num[i] != t[i]:
                    newstr = self.formStr(num, i, k)
                    minTransform = min(dfs(newstr) + 1, minTransform)
            dp[num] = minTransform
            return minTransform

        res = dfs(s)
        return res if res != float("inf") else -1




sol = Solution()
s = "147"
t = "215"
print(sol.transform(s, t, 2))

