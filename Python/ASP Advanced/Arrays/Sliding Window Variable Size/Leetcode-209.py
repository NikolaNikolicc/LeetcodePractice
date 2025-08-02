# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        L, total = 0, 0
        minLen, currLen = len(nums) + 1, 0
        for R in range(len(nums)):

            total += nums[R]
            currLen += 1

            while total >= target:
                minLen = min(minLen, currLen)
                total -= nums[L]
                currLen -= 1
                L += 1

        return minLen if minLen != len(nums) + 1 else 0