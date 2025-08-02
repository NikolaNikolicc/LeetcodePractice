from typing import List
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        print(adj)
        print(indegree)
        
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        print(q)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []

sol = Solution()
edges = [[1,2],[1,3],[3,4],[2,4]]
sol.findRedundantConnection(edges)