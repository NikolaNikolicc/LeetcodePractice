# https://www.youtube.com/watch?v=Vn2v6ajA7U0&t=4s&ab_channel=NeetCode

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        
        nums = sorted(nums)
        def dfs(i):
            print(i)
            if i == len(nums):
                subsets.append(subset[:])
                return

            j = i
            subset.append(nums[j])
            j += 1
            dfs(j)
            subset.pop()

            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1

            dfs(j)

        
        dfs(0)
        return subsets