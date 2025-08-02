class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        l = len(gas) - 1
        r = 0
        price = gas[l] - cost[l]
        while l > r:

            if price < 0:
                l = l - 1
                price += gas[l] - cost[l]
            else:
                price += gas[r] - cost[r]
                r = r + 1
            
        return l if price >= 0 else -1