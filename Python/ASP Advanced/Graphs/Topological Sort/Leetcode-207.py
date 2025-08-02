class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjList = {}

        if len(prerequisites) == 0:
            return True

        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)

        visit = set()
        def dfs(node):
            if node in visit:
                return False

            if adjList[node] == []:
                return True

            visit.add(node)

            for nei in adjList[node]:
                if not dfs(nei):
                    return False
                
            visit.remove(node)
            adjList[node] = []

            return True

        for key in adjList:
            if not dfs(key):
                return False

        return True