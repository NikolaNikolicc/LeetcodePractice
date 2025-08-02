class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # inclusive
        def robber(start, end):
            one, two = 0, 0
            for i in range(start, end + 1):
                newRob = max(one + nums[i], two)
                one = two
                two = newRob

            return two

        if len(nums) == 1:
            return nums[0]

        return max(robber(0, len(nums) - 2), robber(1, len(nums) - 1))