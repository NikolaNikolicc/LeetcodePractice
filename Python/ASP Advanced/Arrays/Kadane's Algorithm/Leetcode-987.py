# https://leetcode.com/problems/longest-turbulent-subarray/description/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) <= 1:
            return len(arr)
        
        maxLen, currLen = 1, 1

        status = not (arr[0] < arr[1])

        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                currLen = 1
                if i + 1 < len(arr):
                    status = not (arr[i] < arr[i + 1])
                continue

            if status:
                if arr[i - 1] <= arr[i]:
                    currLen = 2
                else:
                    currLen += 1
                    status = not status
            else:
                if arr[i - 1] >= arr[i]:
                    currLen = 2
                else:
                    currLen += 1
                    status = not status
            maxLen = max(maxLen, currLen)
        return maxLen