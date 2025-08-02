# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1533575298/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for elem in nums:
            if l == 0 or l == 1 or nums[l - 2] != elem:
                nums[l] = elem
                l += 1

        return l