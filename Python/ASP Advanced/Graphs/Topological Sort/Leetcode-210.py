class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}

        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])

        visited = set()
        path = set()
        output = []
        def dfs(node):
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

        for node in range(numCourses):
            if not dfs(node):
                return []

        return output