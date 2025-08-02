class UnionFind:
    def __init__(self, n):
        self.par = {elem:elem for elem in range(n)}
        self.rank = [0] * n
        self.numComponents = n

    def find(self, node):
        curr = self.par[node]
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
        elif self.rank[par1] < self.rank[par2]:
            self.par[par1] = par2
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        self.numComponents -= 1    
            
            
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        return uf.numComponents
