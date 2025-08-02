class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        s1, s2 = s, t

        # initialize first row
        old = [0] * (len(s2) + 1)
       
        old[-1] = 1

        print(old)
        for i1 in range(len(s1) - 1, -1, -1):
            new = [0] * (len(s2) + 1)
            new[-1] = 1
            for i2 in range(len(s2) - 1, -1, -1):
                new[i2] = old[i2]
                if s1[i1] ==  s2[i2]:
                    new[i2] += old[i2 + 1]

            old = new[:]
            print(old)

        return old[0]

sol = Solution()
s="xxyxy"
t="xy"
print(sol.numDistinct(s, t))

# caat
# caaat
# (caa)a(t)
# (ca)a(at)
# (c)a(aat)