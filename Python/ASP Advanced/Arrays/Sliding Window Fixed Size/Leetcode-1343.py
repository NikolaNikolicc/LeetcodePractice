# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        output = 0
        L = 0

        currSum = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1

            currSum += arr[R]
            if R - L + 1 == k and currSum/k >= threshold:
                output += 1

        
        return output
