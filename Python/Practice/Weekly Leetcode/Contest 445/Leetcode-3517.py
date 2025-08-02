
class Solution(object):
    def smallestPalindrome(self, s):
        chars = [0 for _ in range(26)]

        for ch in s:
            chars[ord(ch) - ord("a")] += 1

        odd = -1
        for i in range(26):
            if chars[i] % 2:
                odd = i
                chars[i] -= 1

        start = ""
        for i in range(26):
            while chars[i]:
                start += chr(i + ord("a"))
                chars[i] -= 2


        return start + chr(odd + ord("a")) + start[::-1] if odd != -1 else start + start[::-1]

sol = Solution()
s = "z"
print(sol.smallestPalindrome(s))