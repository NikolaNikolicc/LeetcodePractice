from typing import List

class Solution:

    def maxCoinsRecursive(self, nums: List[int]) -> int:
        
        def dfs(l: List[int]) -> int:
            cpy = l[:]
            maxVal = 0
            for i in range(len(l)):
                cpy.pop(i)
                
                left = l[i - 1] if i > 0 else 1
                middle = l[i]
                right = l[i + 1] if i < len(l) - 1 else 1
                
                val = left * middle * right
                maxVal = max(maxVal, dfs(cpy) + val)

                cpy.insert(i, l[i])

            return maxVal

        return dfs(nums)
    
    # we are reversing logic, we are popping the ballon at certain position last
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dfs(l: int, r: int) -> int:

            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]
            
            maxVal = 0
            for i in range(l, r + 1):

                val = nums[l - 1] * nums[i] * nums[r + 1]

                maxVal = max(maxVal, dfs(l, i - 1) + dfs(i + 1, r) + val)

            cache[(l, r)] = maxVal
            return cache[(l, r)]
        
        return dfs(1, len(nums) - 2)