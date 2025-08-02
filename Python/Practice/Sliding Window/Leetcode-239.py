from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        markElems = []

        l = 0

        maximums = []
        for r in range(len(nums)):
            heapq.heappush(heap, -nums[r])

            if r - l + 1 == k:
                maximums.append(-heap[0])
                heapq.heappush(markElems, -nums[l])
                l += 1

            while heap and markElems and heap[0] == markElems[0]:
                heapq.heappop(heap)
                heapq.heappop(markElems)

        return maximums