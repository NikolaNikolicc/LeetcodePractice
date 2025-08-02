class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj = {i:[] for i in range(numCourses)}

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])

        prereq = []
        visited = set()
        def dfs(node):
            if node in visited:
                return 

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

            prereq.append(node)

        pre = {}
        for node in range(numCourses):
            prereq = []
            visited = set()
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            pre[node] = prereq[:]

        ret = []
        for query in queries:
            if query[0] in pre[query[1]]:
                ret.append(True)
            else:
                ret.append(False)

    def checkIfPrerequisiteSimple(self, numCourses, prerequisites, queries):
        adj = {i:[] for i in range(numCourses)}

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])

        pre = {i: set() for i in range(numCourses)}
        visited = set()
        print(adj)
        def dfs(node):

            if node in visited:
                return pre[node]
            
            for nei in adj[node]:
                pre[nei] = dfs(nei)
                pre[node] |= pre[nei]
                pre[node].add(nei)

            visited.add(node)
            return pre[node]

        for i in range(numCourses):
            dfs(i)

        ret = []
        for query in queries:
            if query[0] in pre[query[1]]:
                ret.append(True)
            else:
                ret.append(False)

        return ret

sol = Solution()
n = 3
prereq = [[1,2],[1,0],[2,0]]
q = [[1,0],[1,2]]
print(sol.checkIfPrerequisite(n, prereq, q))
