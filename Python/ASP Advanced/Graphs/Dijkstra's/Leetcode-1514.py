import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        adj = {i:[] for i in range(n)}

        for i, edge in enumerate(edges):
            adj[edge[0]].append((succProb[i], edge[1]))
            adj[edge[1]].append((succProb[i], edge[0]))

        maxHeap = [(-1, start_node)]
        greatest = {i:0 for i in range(n)}
        while maxHeap and greatest[end_node] == 0:
            val, src = heapq.heappop(maxHeap)
            val = -val

            if greatest[src] != 0:
                continue

            greatest[src] = val

            for w, dst in adj[src]:
                if greatest[dst] == 0:
                    heapq.heappush(maxHeap, (-val*w, dst))

        return greatest[end_node]

sol = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start_node = 0
end_node = 2
print(sol.maxProbability(n, edges, succProb, start_node, end_node))