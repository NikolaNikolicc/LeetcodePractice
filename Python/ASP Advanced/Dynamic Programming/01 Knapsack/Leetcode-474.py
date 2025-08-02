from collections import defaultdict

class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = defaultdict(int)

        for s in strs:
            ones, zeroes = s.count("1"), s.count("0")
            for i in range(n, ones - 1, -1):
                for j in range(m, zeroes - 1, -1):
                    dp[(i, j)] = max(dp[(i, j)], 1 + dp[(i - ones, j - zeroes)])

        return dp[(n, m)]

# [[0, 0, 0, 0], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1]]

# [[0, 0, 0, 0], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1], 
# [0, 1, 1, 1], 
# [0, 1, 2, 2], 
# [0, 1, 2, 2]]

# [[0, 1, 1, 1], 
# [0, 1, 2, 2], 
# [0, 1, 2, 2], 
# [0, 1, 2, 2], 
# [0, 1, 2, 3], 
# [0, 1, 2, 3]]

# [[0, 1, 1, 1], 
# [1, 2, 2, 2], 
# [1, 2, 3, 3], 
# [1, 2, 3, 3], 
# [1, 2, 3, 3], 
# [1, 2, 3, 4]]

sol = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(sol.findMaxForm(strs, m, n))