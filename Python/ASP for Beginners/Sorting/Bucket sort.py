# It is used for specified range of values
# Bucket sort is basically UNSTABLE, but if we modify it so we can use linked lists it can be STABLE

# leetcode-75
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums):
        # 0-red, 1-white, 3-blue
        colorCnt = [0, 0, 0]
        for elem in nums:
            if elem == 0:
                colorCnt[0] += 1
            elif elem == 1:
                colorCnt[1] += 1
            elif elem == 2:
                colorCnt[2] += 1
        pos = 0
       
        for index in range(len(colorCnt)):
            for cnt in range(colorCnt[index]):
                nums[pos] = index
                pos += 1
