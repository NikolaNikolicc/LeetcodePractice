# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashSet = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                hashSet.remove(nums[L])
                L += 1

            if nums[R] in hashSet:
                return True
            
            hashSet.add(nums[R])
        return False