import heapq
import math

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # print(adj)

        minHeap = []
        for w, u in adj[0]:
            heapq.heappush(minHeap, (w, u))

        visited = set()
        mst = 0
        visited.add(0)

        n = len(points)
        while minHeap and len(visited) != n:

            w, u = heapq.heappop(minHeap)

            if u in visited:
                continue

            mst += w
            visited.add(u)

            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (w, v))

        return mst

sol = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(sol.minCostConnectPoints(points))