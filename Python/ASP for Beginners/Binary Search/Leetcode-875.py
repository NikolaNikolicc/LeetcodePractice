import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        
        # Initialize
        maxVal = max(piles)

        def isValid(k):
            # num of occurances in each elem should be <= h
            occurances = 0
            for elem in piles:
                occurances += math.ceil(float(elem) / k)
                if occurances > h:
                    return False
            return True

        # BinarySearch
        s, e = 1, maxVal
        res = maxVal
        while s <= e:
            mid = (s + e) // 2

            if isValid(mid):
                e = mid - 1
                res = mid
            else:
                s = mid + 1

        return res

# [30,11,23,4,20]
# h = 5, max = 30
# s = 1, e = 30
# mid = 15

sol = Solution()
array = [30,11,23,4,20]
print(sol.minEatingSpeed(array, 5))