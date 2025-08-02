from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        l = []
        def dfs(pos):
            print(pos)
            if sum(l) == target:
                output.append(l[:])
                return
            elif sum(l) > target or pos >= len(candidates):
                return
            
            l.append(candidates[pos])
            dfs(pos + 1)
            l.pop()

            pos += 1
            while pos < len(candidates) and candidates[pos - 1] == candidates[pos]:
                pos += 1

            dfs(pos)

        dfs(0)
        return output
    
sol = Solution()
candidates = [9,2,2,4,6,1,5]
target = 8

print(sol.combinationSum2(candidates, target))