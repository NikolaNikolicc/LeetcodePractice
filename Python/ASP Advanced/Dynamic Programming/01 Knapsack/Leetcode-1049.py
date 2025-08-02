class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        target = sum(stones) // 2

        s = 1
        for stone in stones:
            s |= s << stone

        while s & (1 << target) == 0:
            target -= 1

        return sum(stones) - target - target


sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeightII(stones))