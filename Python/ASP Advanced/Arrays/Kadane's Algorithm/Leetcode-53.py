# https://leetcode.com/problems/maximum-subarray/description/

class Solution:

    def maxSubArrayOptimal(self, nums: List[int]) -> int:
        maxSum, currSum = -1001, 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += num
            maxSum = max(currSum, maxSum)

        return maxSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]

            if currSum + n < currSum and currSum + n < 0:
                currSum = n
            else:
                currSum = max(currSum + n, n)
                
            maxSum = max(currSum, maxSum)

        return maxSum