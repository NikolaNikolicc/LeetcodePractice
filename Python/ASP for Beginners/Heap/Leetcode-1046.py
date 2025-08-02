# https://leetcode.com/problems/last-stone-weight/description/

from typing import List

class Solution:

    def bucket(self, stones):
        
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1
        
        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            print(j)
            while j > 0 and bucket[j] == 0:
                j -= 1
            print(j)
            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first

    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-weight for weight in stones]
        heapq.heapify(maxheap)
        while(len(maxheap) > 1):
            val1 = heapq.heappop(maxheap)
            val2 = heapq.heappop(maxheap)

            smash = val1 - val2

            if smash:
                heapq.heappush(maxheap, smash)

        return -maxheap[0] if len(maxheap) > 0 else 0


# 2 4 37 37 37

# 2 4 37
# 1 1 3

sol = Solution()
print(sol.bucket([2, 4, 37, 37]))
