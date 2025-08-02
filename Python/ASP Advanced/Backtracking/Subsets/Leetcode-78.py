class Solution(object):
    def subsets(self, nums):
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