# https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        adjListOpposite = {}

        if len(prerequisites) == 0:
            return True

        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = set()
            if dst not in adjList:
                adjList[dst] = set()
            adjList[src].add(dst)

            if src not in adjListOpposite:
                adjListOpposite[src] = set()
            if dst not in adjListOpposite:
                adjListOpposite[dst] = set()
            adjListOpposite[dst].add(src)

        q = deque()
        
        nodeCnt = 0
        for elem in adjList:
            if len(adjList[elem]) == 0:
                q.append(elem)
                nodeCnt += 1

        cnt = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in adjListOpposite[node]:
                    adjList[nei].remove(node)
                    if len(adjList[nei]) == 0:
                        q.append(nei)
                        nodeCnt += 1
        
            cnt += 1

        if len(adjList) == nodeCnt and cnt <= numCourses:
            return True
        else:
            return False