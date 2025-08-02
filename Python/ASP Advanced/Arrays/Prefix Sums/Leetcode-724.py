# https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndexSpaceOptimized(self, nums):
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1
    
    def pivotIndex(self, nums):
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] + prefix[i]

        total = sum(nums)
        for i in range(len(nums)):
            if prefix[i] == (total - prefix[i + 1]):
                return i

        return -1

sol = Solution()
nums = [1,7,3,6,5,6]
sol.pivotIndex(nums)