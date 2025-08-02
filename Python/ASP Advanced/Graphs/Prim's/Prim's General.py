class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        minHeap = []

        for w, dst in adj[0]:
            heapq.heappush(minHeap, (w, dst))

        visited = set()
        mst = 0
        visited.add(0)

        while minHeap and len(visited) != n:

            w, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            mst += w

            for w, dst in adj[node]:
                heapq.heappush(minHeap, (w, dst))

        return mst if len(visited) == n else -1

