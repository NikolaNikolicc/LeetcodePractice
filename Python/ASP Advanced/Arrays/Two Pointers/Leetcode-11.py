# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(l, r):
            return min(heights[l], heights[r]) * (r - l)
        
        l, r = 0, len(heights) - 1

        maxArea = 0
        while l < r:
            currLen = calcArea(l, r)
            maxArea = max(maxArea, currLen)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea