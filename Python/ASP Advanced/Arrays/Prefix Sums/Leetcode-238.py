# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

class Solution:

    def productExceptSelfOptimal(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]

        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        carry = 1
        for i in range(len(nums)):
            if i > 0:
                res[i] = res[i - 1] * carry

            carry = nums[i]

        res1 = [1] * len(nums)
        carry = 1
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                res1[i] = res1[i + 1] * carry

            carry = nums[i]

        for i in range(len(nums)):
            res[i] *= res1[i]

        return res

sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))