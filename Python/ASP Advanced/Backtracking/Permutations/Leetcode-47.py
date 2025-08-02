from collections import Counter

class Solution(object):

    def permuteUniqueMostEfficient(self, nums):
        res = []
        nums.sort()  # Sort to group duplicates
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            used = set()  # Track used elements at this position
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue  # Skip duplicates
                used.add(nums[i])
                
                # Swap and recurse
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # Undo swap immediately
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res
    
    def permuteUniqueHashMap(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = Counter(nums)

        final = []
        res = []
        def backtrack():
            if len(res) == len(nums):
                final.append(res[:])
                return
            for num in counter:
                if counter[num] > 0:
                    res.append(num)
                    counter[num] -= 1
                    backtrack()
                    counter[num] += 1
                    res.pop()

        backtrack()
        return final
        

sol = Solution()
nums = [1, 1, 2]
print(sol.permuteUnique(nums))