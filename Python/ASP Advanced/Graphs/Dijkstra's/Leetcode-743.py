class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjecency = {i:[] for i in range(1, n + 1)}

        for src, dst, t in times:
            adjecency[src].append((dst, t))

        minHeap = [(0, k)]

        shortest = {i: "inf" for i in range(1, n + 1)}

        while minHeap:
            w1, node = heapq.heappop(minHeap)

            if shortest[node] < w1:
                continue

            shortest[node] = w1

            for dst, w2 in adjecency[node]:
                if shortest[dst] > w1 + w2:
                    heapq.heappush(minHeap, (w1 + w2, dst))


        ret = max(shortest.values())
        return ret if ret != float("inf") else -1