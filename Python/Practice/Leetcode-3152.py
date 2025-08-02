class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        sums = [0]
        currSum = 0
        for n in range(1, len(nums)):
            if (nums[n - 1] ^ nums[n]) & 1: 
                currSum += 1
            sums.append(currSum)

        ret = []
        print(sums)
        print(currSum)
        for query in queries:
            if sums[query[1]] - sums[query[0]] < query[1] - query[0]:
                ret.append(False)
            else:
                ret.append(True)

        return ret
        

sol = Solution()
nums = [1, 1]
queries = [[0,1]]
print(sol.isArraySpecial(nums, queries))

# prefix sums method