class Solution(object):

    def longestPalindromeSubseqNew(self, s):
        
        cache = {}
        def pali(l, r):
            if l < 0 or r >= len(s):
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]

            if s[l] == s[r]:
                add = 1 if l == r else 2
                cache[(l, r)] = add + pali(l - 1, r + 1)
            else:
                cache[(l, r)] = max(pali(l - 1, r), pali(l, r + 1))
            
            return cache[(l, r)]

        longest = 0
        for i in range(len(s)):
            
            longest = max(longest, pali(i, i))
            
            longest = max(longest, pali(i, i + 1))

        return longest
    
    def longestPalindromeSubseq(self, s):
        
        def pali(l, r):   
            longest = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest += 2
                l -= 1
                r += 1
                
            longest_1, longest_2 = 0, 0
            if r + 1 < len(s) and l >= 0:
                longest_1 = pali(l, r + 1)
            if l - 1 >= 0 and r < len(s):
                longest_2 = pali(l - 1, r)

            longest += max(longest_1, longest_2)
            
            return longest

            

        maxLen = 0
        for i in range(len(s)):
            
            l = pali(i - 1, i + 1) + 1
            maxLen = max(maxLen, l)

            l = pali(i, i + 1)
            maxLen = max(maxLen, l)

        return maxLen

# bbbab

# l = 0
# r = 0
sol = Solution()
s = "bbbab"
print(sol.longestPalindromeSubseq(s))