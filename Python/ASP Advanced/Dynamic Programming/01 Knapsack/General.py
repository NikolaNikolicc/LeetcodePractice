from typing import List

class Solution:

    def maximumProfitShortest(self, profit: List[int], weight: List[int], capacity: int) -> int:
        helper = [0] * (capacity + 1)

        for p in range(len(profit)):
            new = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                if c - weight[p] >= 0:
                    new[c] = max(helper[c - weight[p]] + profit[p], helper[c])
                else:
                    new[c] = helper[c]
            helper = new

        return helper[-1]
    
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        helper = [[0]*(capacity + 1)]*2

        for i in range(capacity + 1):
            if i - weight[0] >= 0:
                helper[0][i] = profit[0]
        
        print(helper)
        for i in range(1, len(profit)):
            helper[1] = [0]*(capacity + 1)
            for j in range(1, capacity + 1):
                fst = helper[0][j]
                sec = 0
                if j - weight[i] >= 0:
                    sec = profit[i] + helper[0][j - weight[i]]
                helper[1][j] = max(fst, sec)
            print(helper)
            helper[0] = helper[1][:]

        return helper[1][-1]

profit=[4,4,7,1]
weight=[5,2,3,1]
capacity=8
sol = Solution()
sol.maximumProfit(profit, weight, capacity)