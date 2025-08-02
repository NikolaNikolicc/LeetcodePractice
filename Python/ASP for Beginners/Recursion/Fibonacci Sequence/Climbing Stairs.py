# 1
# 1 x2

# 2
# 1 2
# 1 x2

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n

            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(1 + i) + dfs(2 + i)
            return cache[i]

        return dfs(0)

            
        # bottom-up solution
        # if n == 0:
        #     return 1

        # one, two = 0, 0
        # if n - 1 >= 0:
        #     one = self.climbStairs(n - 1)

        # if n - 2 >= 0:
        #     two = self.climbStairs(n - 2)
        
        # return one + two

# 3

# 1 + 1 + 1
# 1 + 2
# 2 + 1

sol = Solution()
print(sol.climbStairs(3))