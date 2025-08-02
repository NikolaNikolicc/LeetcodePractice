from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        target = total // 2
        if float(total) / 2 != target:
            return False

        sums = set([0])
        for i in range(len(nums) - 1, -1, -1):
            newSums = set()
            for s in sums:
                if s == target:
                    return True
                
                newSums.add(nums[i])
                newSums.add(nums[i] + s)
            sums = newSums
        return False

nums = [1,2,3,4]
sol = Solution()
print(sol.canPartition(nums))