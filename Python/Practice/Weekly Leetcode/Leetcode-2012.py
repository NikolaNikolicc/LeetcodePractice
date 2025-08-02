class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return 0
        
        ret = [0]*len(nums)

        maxVal, prev = nums[0], nums[0]

        for i in range(1, len(nums) - 1):
            if nums[i] > maxVal:
                ret[i] = 2
            elif nums[i] <= maxVal and nums[i] > prev:
                ret[i] = 1
            maxVal = max(maxVal, nums[i])
            prev = nums[i]

        minVal, prev = nums[-1], nums[-1]
        print(ret)
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] < minVal:
                ret[i] = min(ret[i], 2)
            elif nums[i] >= minVal and nums[i] < prev:
                ret[i] = min(ret[i], 1)
            else:
                ret[i] = 0
            minVal = min(minVal, nums[i])
            prev = nums[i]
        
        return sum(ret)