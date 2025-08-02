class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {elem: elem for elem in range(len(edges) + 1)}
        rank = {elem: 0 for elem in range(len(edges) + 1)}

        def find(node):
            curr = par[node]
            while curr != par[curr]:
                curr = par[par[curr]]
                curr = par[curr]
            return curr

        ret = edges[0]
        for edge in edges:
            fst, sec = edge[0], edge[1]
            par1, par2 = find(fst), find(sec)
            if par1 == par2:
                ret = edge
            else:
                if rank[par1] > rank[par2]:
                    par[par2] = par1
                elif rank[par2] > rank[par1]:
                    par[par1] = par2
                else:
                    par[par2] = par1
                    rank[par1] += 1

            print(par)
        return ret