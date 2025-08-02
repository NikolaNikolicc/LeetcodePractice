class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getDigit(number):
            lst = []
            while number > 0:
                lst.append(number % 10)
                number /= 10

            return lst

        
        digits = []
        for i in range(len(nums)):
            digits.append(getDigit(nums[i]))

        print(digits)

sol = Solution()
nums = [13, 23, 12]
sol.sumDigitDifferences(nums)