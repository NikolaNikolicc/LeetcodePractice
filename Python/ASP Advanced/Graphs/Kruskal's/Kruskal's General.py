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
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]

        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda edge: edge[2])

        uf = UnionFind(n)
        mst = 0
        for edge in edges:
            if uf.union(edge[0], edge[1]):
               mst += edge[2]

        return mst if max(uf.rank) == n else -1 
