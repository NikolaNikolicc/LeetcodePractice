from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []  # Max heap
        minCapital = [(c, p) for c, p in zip(capital, profits)]  # Min heap
        heapq.heapify(minCapital)
        print(minCapital)
        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                break
            
            w += -heapq.heappop(maxProfit)

        return w

sol = Solution()
k = 2
w = 0
profits = [2, 1, 3]
capital = [12, 12, 13]
sol.findMaximizedCapital(k, w, profits, capital)