# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for index in range(1, len(nums)):
            if(nums[current] != nums[index]):
                current += 1
                nums[current] = nums[index]
        return current + 1 

