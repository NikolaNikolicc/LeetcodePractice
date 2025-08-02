# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        def isChar(c):
            return (ord("0") <= ord(c) and ord(c) <= ord("9")) or \
                 (ord("a") <= ord(c) and ord(c) <= ord("z"))
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isChar(s[l]):
                l += 1

            while l < r and not isChar(s[r]):
                r -= 1
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True