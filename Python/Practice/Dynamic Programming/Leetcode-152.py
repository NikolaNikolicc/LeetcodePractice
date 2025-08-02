class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd, minProd = nums[0], nums[0]
        res = maxProd
        for i in range(1, len(nums)):
            tmp = maxProd * nums[i]
            maxProd = max(maxProd * nums[i], nums[i], minProd * nums[i])
            minProd = min(tmp, nums[i], minProd * nums[i])
            res = max(res, maxProd)

        return res
