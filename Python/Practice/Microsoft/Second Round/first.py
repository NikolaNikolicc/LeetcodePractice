from typing import List

class Solution:
    def findMinimum(self, nums: List[int])->List[int]:

        res = [0]*len(nums)

        indices = [i for i in range(len(nums))]
        indices.sort(key = lambda i: nums[i])

        maxIndex = indices[0]
        for i in range(len(indices)):
            maxIndex = max(maxIndex, indices[i])
            res[indices[i]] = maxIndex

        return res

sol = Solution()
nums = [1, 3, 9, 4, 2, 5, 6]
print(sol.findMinimum(nums))