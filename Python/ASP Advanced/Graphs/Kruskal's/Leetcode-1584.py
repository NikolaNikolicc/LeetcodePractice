from typing import List

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(i, j):
            return abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
        
        pairs = []
        for i in range(len(points)):

            for j in range(len(points)):
                pairs.append([i, j, dist(i, j)])

        pairs.sort(key = lambda pair: pair[2])
        print(pairs)

        uf = UnionFind(len(points))
        mst = 0
        for pair in pairs:
            if uf.union(pair[0], pair[1]):
               mst +=  pair[2]

        return mst

sol = Solution()
points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
print(sol.minCostConnectPoints(points))