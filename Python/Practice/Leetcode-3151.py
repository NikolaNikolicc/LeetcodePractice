class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for n in range(len(nums)  - 1):
            if not ((nums[n] ^ nums[n + 1]) & 1):
                return False
        return True