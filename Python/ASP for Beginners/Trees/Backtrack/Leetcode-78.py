# https://leetcode.com/problems/subsets/description/

# ol: [[], [1], [1, 2], [1, 2, 3]]
# lst: [2]
# unvisited: [2, 3]

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outputList = [[]]

        def dfs(lst, unvisited):
            for i in range(len(unvisited)):
                if len(unvisited) > 0:
                    elem = unvisited.pop(0)
                    lst.append(elem)
                    outputList.append(lst[:])
                    dfs(lst, unvisited[:])
                    lst.pop()
                    # unvisited.append(elem)


        dfs([], nums)
        return outputList

sol = Solution()
print(sol.subsets([1, 2, 3]))