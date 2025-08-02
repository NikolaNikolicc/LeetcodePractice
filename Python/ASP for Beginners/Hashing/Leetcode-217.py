# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashSet = set()
        for elem in nums:
            if elem not in hashSet:
                hashSet.add(elem)
            else:
                return True
        return False