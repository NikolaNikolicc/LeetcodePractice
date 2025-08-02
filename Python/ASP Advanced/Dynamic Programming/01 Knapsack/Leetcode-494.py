class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            newdp = defaultdict(int)
            for key, value in dp.items():
                newdp[key + num] += value
                newdp[key - num] += value
            dp = newdp

        return dp[target]