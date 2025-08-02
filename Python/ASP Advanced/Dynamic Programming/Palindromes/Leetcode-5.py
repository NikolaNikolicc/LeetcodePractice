class Solution(object):
    def longestPalindrome(self, s):
        if s == "":
            return s
        
        maxLen = 1
        substring = s[0]
        for i in range(len(s)):
            
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 + 1> maxLen:
                    maxLen = r - l + 1
                    substring = s[l:r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1> maxLen:
                    maxLen = r - l + 1
                    substring = s[l:r + 1]
                l -= 1
                r += 1

        return substring

sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))