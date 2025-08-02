# https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:    
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[index] = nums[i]
                index += 1
        return index
        
    def removeElementFirst(self, nums: List[int], val: int) -> int:
        if(len(nums) == 0): return 0
        end = len(nums) - 1
        while(nums[end] == val):
            end -= 1
            if(end < 0): return 0
        start = 0
        while start < end:
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = val
                end -= 1
                while(nums[end] == val):
                    end -= 1
                    if(end < 0): return 0
            start += 1
            print(end)
        if(nums[end] == val): return 0
        return end  + 1

sol = Solution()
nums = [4, 5]
sol.removeElement(nums, 5)
print(nums)