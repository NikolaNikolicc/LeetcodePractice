# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenationFirst(self, nums: List[int]) -> List[int]:
        return 2*nums

    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for elem in nums:
                ans.append(elem)
        return ans