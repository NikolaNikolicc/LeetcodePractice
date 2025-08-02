# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashMap = {}

        def findMaxFreq():
            maxv = -1
            for key in hashMap.keys():
                maxv = max(maxv, hashMap[key])
            return maxv
        
        

        l = 0
        maxLen, currLen = 0, 0

        for r in range(len(s)):

            if s[r] not in hashMap:
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1

            currLen += 1

            maxFreq = findMaxFreq()
            if currLen - maxFreq <= k:
                maxLen = max(maxLen, currLen)
            else:
                hashMap[s[l]] -= 1
                l += 1
                currLen -= 1

            maxLen = max(maxLen, currLen)

        return maxLen

    def characterReplacementShorter(self, s, k):
        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            maxf  = max(count.values())

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

    def characterReplacementOptimal(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# AABABBA
# # maxf = 3 
# A: 2 B: 2