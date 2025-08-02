class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = [-1 for _ in range(len(queries))]

        indices = [i for i in range(len(queries))]
        indices.sort(key = lambda i: queries[i])

        heap = []

        intervals.sort()

        i = 0
        for index in indices:
            value = queries[index]

            while i < len(intervals) and intervals[i][0] <= value:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(heap, (end - start + 1, start, end))
                i += 1

            while heap and not (heap[0][1] <= value <= heap[0][2]):
                heapq.heappop(heap)

            if heap:
                output[index] = heap[0][0]

        return output
