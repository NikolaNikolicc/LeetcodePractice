from typing import List

class Solution:

    def searchSimplified(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[l] <= nums[mid] and nums[l] > target:
                l = mid + 1
            elif nums[r] >= nums[mid] and nums[r] < target:
                r = mid - 1
            else:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[l] <= nums[mid] and (nums[l] > target or target > nums[mid]):
                l = mid + 1
            elif nums[r] >= nums[mid] and (nums[r] < target or target < nums[mid]):
                r = mid - 1
            else:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
nums=[5,1,2,3,4]
target=1
sol = Solution()
print(sol.search(nums, target))