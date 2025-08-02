
class Solution(object):

    # working on leetcode
    def validSolution(self, n, m, group, beforeItems):
        maxGroup = max(group) + 1

        for g in range(len(group)):
            if group[g] == -1:
                group[g] = maxGroup
                maxGroup += 1

        # print(groups)
        coursePrereqByGroup = {i: {} for i in range(maxGroup)}
        groupPrereq = {i: [] for i in range(maxGroup)}

        for i in range(len(beforeItems)):
            coursePrereqByGroup[group[i]][i] = []
            for elem in beforeItems[i]:
                if group[elem] != group[i]:
                    groupPrereq[group[i]].append(group[elem])
                else:
                    coursePrereqByGroup[group[i]][i].append(elem)

        print(coursePrereqByGroup)
        print(groupPrereq)

        def topoSort(adj):
            output = []

            visited = set()
            path = set()
            def dfs(elem):
                
                if elem in path:
                    return False
                
                if elem in visited:
                    return True
                
                path.add(elem)
                visited.add(elem)
                for nei in adj[elem]:
                    if not dfs(nei):
                        return False
                path.remove(elem)
                output.append(elem)

                return True

            for elem in adj:
                if not dfs(elem):
                    return []
                
            return output
        
        groupOrder = topoSort(groupPrereq)
        # print(groupOrder)

        final = []
        for g in groupOrder:
            # print(coursePrereqByGroup[g])
            res = topoSort(coursePrereqByGroup[g])
            if res == [] and g in group:
                return []
            final += res

        return final
    
    def sortItems(self, n, m, group, beforeItems):
        adjGroup = {i:{} for i in range(m)}
        adjGroup[-1] = {}

        for i in range(n):
            adjGroup[group[i]][i] = beforeItems[i]

        print(adjGroup)

        topologicalSort = []
        visitedGroup = set()
        visitedNodes = set()
        
        def sortGroup(g, node):

            if node in visitedNodes:
                return

            for nei in adjGroup[g][node]:
                if group[nei] != g and group[nei] in visitedGroup:
                    continue
                elif group[nei] != g:
                    dfs(group[nei], nei)

                sortGroup(g, nei)

            visitedNodes.add(node)
            topologicalSort.append(node)    
            
        
        def dfs(g, node):

            if g == -1:
                sortGroup(-1, node)
            if g != -1:
                for id, prereqs in adjGroup[g].items():
                    for prereq in prereqs:
                        if prereq not in adjGroup[g]:
                            dfs(group[prereq], prereq)

                for id in adjGroup[g]:
                    sortGroup(g, id)

                    

        for g in adjGroup:
            for id in adjGroup[g]:
                dfs(g, id)

            visitedGroup.add(g)

        return topologicalSort

sol = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(sol.sortItems(n, m, group, beforeItems))

# maximum recursion depth exceeded