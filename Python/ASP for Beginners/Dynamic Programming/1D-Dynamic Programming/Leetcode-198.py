class Solution:

    def rob1(self, nums: List[int]) -> int:

        cache = nums[:]
        # cache = [2, 9, 8, 3, 6]
        # nums =  [2, 9, 8, 3, 6]

        for i in range(len(nums) - 1, -1, -1):
            if i + 3 < len(nums):
                cache[i] = max(cache[i + 2] + cache[i], cache[i + 3] + nums[i])
            elif i + 2 < len(nums):
                cache[i] = cache[i + 2] + nums[i]
            else:
                cache[i] = nums[i]
        

    # Space and time optimal solution
    def rob(self, nums: List[int]) -> int:

        one, two = 0, 0
        for num in nums:
            tmp = max(num + one, two)
            one = two
            two = tmp

        return two


# [2,9,8,3,6]