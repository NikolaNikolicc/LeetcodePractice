# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                if nums[l] != nums[r]:
                    nums[l] = nums[r]
                
        return l + 1
