class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i: i[0])

        curr = 0
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[curr][1]:
                res += 1
                if intervals[i][1] < intervals[curr][1]:
                    curr = i    
            else:
                curr = i
            
        return res