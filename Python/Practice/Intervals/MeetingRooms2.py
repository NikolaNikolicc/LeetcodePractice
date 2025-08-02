
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        
        intervals.sort(key = lambda i: i.start)
        days = []

        for i in range(len(intervals)):
            tmp = []
            while days and days[0] > intervals[i].start:
                elem = heapq.heappop(days)
                tmp.append(elem)

            if not days:
                days.append(intervals[i].end)
            else:
                days[0] = max(days[0], intervals[i].end)

            while tmp:
                elem = tmp.pop(0)
                heapq.heappush(days, elem)

        return len(days)

