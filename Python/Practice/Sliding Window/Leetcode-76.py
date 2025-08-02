from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        charst = Counter(t)
        charss = defaultdict(int)

        cntt, cnts = len(charst), 0
        
        pos = 0
        minLenght = [0, len(s) - 1]
        found = False

        # find first elem
        while pos < len(s) and s[pos] not in charst:
            pos += 1

        for i in range(pos, len(s)):            
            # update dictionary value
            if s[i] in charst:
                charss[s[i]] += 1
                if charss[s[i]] == charst[s[i]]:
                    cnts += 1

            # we want to shift our left pointer until number of elements in window greq than num of elems in string t
            while cntt == cnts:
                # we have all elements in window, now we check for min lenght
                if minLenght[1] - minLenght[0] + 1 >= i - pos + 1:
                    minLenght = [pos, i]
                    found = True

                charss[s[pos]] -= 1
                # maybe the number of this elements is higher than demand for it
                if charss[s[pos]] < charst[s[pos]]:
                    cnts -= 1
                pos += 1
                # we are moving pos until we find element from string t, because we want to minimize our window
                while pos <= i and s[pos] not in charst:
                    pos += 1

        if cntt == cnts:
            if minLenght[1] - minLenght[0] + 1 >= len(s) - pos:
                minLenght = [pos, len(s) - 1]
                found = True
        return s[minLenght[0]:minLenght[1] + 1] if found else ""
            



sol = Solution()
s = "a"
t = "aa"
print(sol.minWindow(s, t))