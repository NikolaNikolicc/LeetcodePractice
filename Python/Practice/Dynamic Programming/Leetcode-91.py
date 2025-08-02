class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 0

        res = 0
        for i in reversed(range(len(s))):
            print(i)
            if s[i] == "0":
                res = 0
            else:
                res = one

            if i + 1 < len(s) and int(s[i:i + 2]) < 27 and s[i] != "0":
                res += two

            one, two = res, one

        return res

sol = Solution()
s = "06"
sol.numDecodings(s)