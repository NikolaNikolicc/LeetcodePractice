class Solution(object):
    # curr:2, 2, 2, 6
    # sum: 2, 4, 6, 12

    def combinationSumOptimal(self, nums, target):
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res    
    
    def combinationSum(self, nums, target):
        nums.sort()

        output = []
        current = []
        def dfs(position, sum):
            print("position: " + str(position) + " sum: " + str(sum) + " curr: " + str(current))
            if sum > target or position == len(nums):
                return

            if sum == target:
                output.append(current[:])
                return

            current.append(nums[position])
            # print("parent" + str(position))
            dfs(position, sum + nums[position])
            current.pop()

            while position + 1 < len(nums) and nums[position + 1] == nums[position]:
                position += 1

            if position + 1 < len(nums) and sum + nums[position + 1] <= target:
                dfs(position + 1, sum)

        dfs(0, 0)

        return output

sol = Solution()
nums = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(nums, target))