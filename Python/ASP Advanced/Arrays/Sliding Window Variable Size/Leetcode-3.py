# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = set()
        maxLen = 0
        for R in range(len(s)):
            
            while s[R] in longest:
                longest.remove(s[L])
                L += 1

            longest.add(s[R])    
            maxLen = max(R - L + 1, maxLen)
        return maxLen