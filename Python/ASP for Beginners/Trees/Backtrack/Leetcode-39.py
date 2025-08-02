# https://leetcode.com/problems/combination-sum/description/

# [2, 5, 6, 9]
# terget = 9
# ol: [[2, 2, 5], [9]]
# lst: [9]
# currSum = 9

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        outputList = []
        lst = []
        def dfs(pos, currSum):
            for i in range(pos, len(nums)):
                if currSum + nums[i] > target:
                    return

                currSum += nums[i]
                lst.append(nums[i])

                if currSum == target:
                    outputList.append(lst[:])
                    lst.pop()
                    return

                dfs(i, currSum)

                lst.pop()
                currSum -= nums[i]
                
        dfs(0, 0)
        return outputList
