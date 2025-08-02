from typing import List

class Solution:
    # backtrack
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
    def partitionMy(self, s: str) -> List[List[str]]:

        def pali(left, right):

            print("left: " + str(left) + " right: " + str(right))

            if left > right:
                return [[]]
            
            outputlist = []
            for i in range(left, right + 1):
                print("i: " + str(i))
                l, r = i, i
                while l >= left and r <= right and s[l] == s[r]:
                    l -= 1
                    r += 1

                print("l: " + str(l) + " r: " + str(r))
                lpali = pali(left, l)
                rpali = pali(r, right)

                
                for lp in lpali:
                    
                    for rp in rpali:
                        outputlist.append(lp + [s[l + 1:r]] + rp)

                if i + 1 <= right and s[i] == s[i + 1]:
                    l, r = i, i + 1
                    while l >= left and r <= right and s[l] == s[r]:
                        l -= 1
                        r += 1

                    lpali = pali(left, l)
                    rpali = pali(r, right)

                    for lp in lpali:                        
                        for rp in rpali:
                            outputlist.append(lp + [s[l + 1:r]] + rp)

            return outputlist
        return pali(0, len(s) - 1)

sol = Solution()
print(sol.partition("aab"))