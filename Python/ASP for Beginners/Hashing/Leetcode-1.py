class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, elem in enumerate(nums):
            if target - elem in hashMap:
                return [hashMap[target - elem], index]
            hashMap[elem] = index

        return []