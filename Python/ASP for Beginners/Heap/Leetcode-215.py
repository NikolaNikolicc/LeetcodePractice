# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSort(s, e):
            pivot = nums[e]
            left = s
            for i in range(s, e):
                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            nums[left], nums[e] = nums[e], nums[left]

            if left == k:
                return pivot
            elif left < k:
                return quickSort(left + 1, e)
            else:
                return quickSort(s, left - 1)

        return quickSort(0, len(nums) - 1)

class SolutionHeap:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]