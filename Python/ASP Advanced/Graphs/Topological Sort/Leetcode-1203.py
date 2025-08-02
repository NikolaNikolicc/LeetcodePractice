from collections import defaultdict

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_adj = defaultdict(list)
        group_adj = defaultdict(list)
        for i in range(n):
            for par in beforeItems[i]:
                item_adj[par].append(i)
                if group[i] != group[par]:
                    group_adj[group[par]].append(group[i])

        print(item_adj)
        print(group_adj)

        itm = self.topo_sort(item_adj, n)
        if not itm: return []
        grp = self.topo_sort(group_adj, m)
        if not grp: return []

        print(itm)
        print(grp)

        grouping = defaultdict(list)
        for i in itm:
            grouping[group[i]].append(i)

        print(grouping)

        res = []
        for g in grp:
            res.extend(grouping[g])

        return res

    def topo_sort(self, adj, N):
        visited = [0] * N
        topo = []

        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 1
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            topo.append(node)
            visited[node] = 2
            return False

        for i in range(N):
            if visited[i] == 0:
                if dfs(i):
                    return []

        return topo[::-1]

sol = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(sol.sortItems(n, m, group, beforeItems))