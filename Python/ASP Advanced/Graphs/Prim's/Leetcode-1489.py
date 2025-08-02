
class UnionFind:
    def __init__(self, n):
        self.par = {i:i for i in range(n)}
        self.rank = [1]*n

    def find(self, x):
        curr = x
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr

    def union(self, x, y):
        par1, par2 = self.find(x), self.find(y)

        if par1 == par2:
            return False
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        elif self.rank[par1] < self.rank[par1]:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        else:
            self.rank[par1] += self.rank[par2]
            self.par[par2] = par1
        return True
        

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        uf = UnionFind(n)

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key = lambda i: i[2])

        mst = 0
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                mst += edge[2]

        crit = []
        pseudoCrit = []
        for i in range(len(edges)):
            uf = UnionFind(n)
            submst = 0
            for j in range(len(edges)):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    submst += edges[j][2]

            if submst > mst or max(uf.rank) < n:
                crit.append(edges[i][3])
                continue

            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            submst = edges[i][2]
            for j in range(len(edges)):
                if uf.union(edges[j][0], edges[j][1]):
                    submst += edges[j][2]

            if submst == mst:
                pseudoCrit.append(edges[i][3])

        return [crit, pseudoCrit]
            

sol = Solution()
n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
print(sol.findCriticalAndPseudoCriticalEdges(n, edges))