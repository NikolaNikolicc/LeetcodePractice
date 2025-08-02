from typing import List
from collections import defaultdict

class Solution:
    def findkLargestFromAbove(self, nums: List[int], k: int):
        heights = defaultdict(int)
        maxHeight = float("-inf")
        for num in nums:
            for h in range(num, max(0, num - k - 1), -1):
                heights[h] += num - h
                if heights[h] >= k:
                    maxHeight = max(maxHeight, h)

        return maxHeight

    def findkLargest(self, nums: List[int], k: int):
        heights = defaultdict(int)

        highest = float("-inf")
        for tree in nums:
            for h in range(tree):
                heights[h] += tree - h
                if heights[h] >= k and highest < h:
                    highest = h

        return highest

sol = Solution()
nums = [2, 5, 4, 3]
print(sol.findkLargestFromAbove(nums, 3))

        