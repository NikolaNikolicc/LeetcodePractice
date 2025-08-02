from typing import List
from collections import defaultdict

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for src1, dst1, price in flights:
            adj[src1].append((price, dst1))

        # return final price
        def backtrack(fr: int, credits: int) -> int:

            if credits > k + 1:
                return -1            

            if fr == dst:
                return 0

            minPrice = float("inf")
            for price, to in adj[fr]:
                res = backtrack(to, credits + 1)
                if res != -1:
                    minPrice = min(minPrice, price + res)

            return minPrice
                    

        res = backtrack(src, 0)
        return res if res != float("inf") else -1