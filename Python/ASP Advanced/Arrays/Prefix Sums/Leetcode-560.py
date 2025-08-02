class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashMap = {0:1}

        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            
            if (total - k) in hashMap:
                res += hashMap[total - k]

            hashMap[total] = 1 + hashMap.get(total, 0)

        return res
        

sol = Solution()
nums = [1, -1, 0]
k = 0
print(sol.subarraySum(nums, k))
