# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        maxSum, minSum = nums[0], nums[0]
        currSumMax, currSumMin = nums[0], nums[0]

        total = nums[0]
        for i in range(1, len(nums)):

            n = nums[i]
            total += n
            
            currSumMax = max(currSumMax + n, n)
            currSumMin = min(currSumMin + n, n)

            maxSum = max(currSumMax, maxSum)
            minSum = min(currSumMin, minSum)

        
        return max(total - minSum, maxSum) if maxSum > 0 else maxSum