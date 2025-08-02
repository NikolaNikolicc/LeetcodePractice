from typing import List

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])

        print(adj)

        output = []
        visited = set()
        path = set()
        def dfs(node):
            # print("node: " + str(node) + " path: " + str(path))
            if node in path:
                return False
            
            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            output.append(node)
            return True

        for i in range(n):
            if not dfs(i):
                return []

        return output[::-1]

n=3
edges=[[0,1],[1,2],[2,0]]
sol = Solution()
print(sol.topologicalSort(n, edges))