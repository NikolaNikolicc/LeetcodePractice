class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n

    def find(self, x: int) -> int:
        curr = self.par[x]
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr

    def union(self, x: int, y: int) -> bool:
        par1, par2 = self.find(x), self.find(y)

        if par1 == par2:
            return False
        
        self.components -= 1
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return False
            # print(uf.rank)

        return uf.components == 1
