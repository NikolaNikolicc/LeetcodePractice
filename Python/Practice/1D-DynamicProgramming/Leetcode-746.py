class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 1:
            return cost[0]
        
        for i in range(len(cost) - 3, -1, -1):
            minCost = min(cost[i + 1], cost[i + 2])
            cost[i] += minCost

        return min(cost[0], cost[1])