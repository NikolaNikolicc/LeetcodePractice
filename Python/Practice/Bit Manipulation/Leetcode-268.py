from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mask = 0

        for num in nums:
            mask |= (1 << num)

        cmpVal = 0

        for i in range(len(nums) + 1):
            cmpVal |= (1 << i)

        final = cmpVal ^ mask

        cnt = -1
        while final:
            cnt += 1
            final >>= 1

        return cnt
    
sol = Solution()
nums = [1, 2, 3]
sol.missingNumber(nums)