class Solution:
    def findDuplicateModifyingArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):

            pos = abs(nums[i]) - 1
            if nums[pos] < 0:
                return abs(nums[i])
            nums[pos] *= -1

    def findDuplicateTwoPointers(self, nums):
    
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        start = 0
        while start != slow:
            slow = nums[slow]
            start = nums[start]

        return slow