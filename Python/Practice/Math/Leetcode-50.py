class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def dfs(deg):
            if deg == 0:
                return 1

            if deg == 1:
                return x

            if deg in cache:
                return cache[deg]

            half = deg // 2

            left = dfs(half)
            right = dfs(deg - half)

            cache[deg] = left * right
            return cache[deg]

        res = dfs(abs(n))
        return res if n >= 0 else 1/res