class UnionFind {
private:
    int n;
    vector<int> Parent, Size;

public:
    UnionFind(int n) : n(n), Parent(n + 1), Size(n + 1, 1) {
        for (int i = 0; i <= n; ++i) {
            Parent[i] = i;
        }
    }

    int find(int node) {
        if (Parent[node] != node) {
            Parent[node] = find(Parent[node]);
        }
        return Parent[node];
    }

    bool unionSets(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false;
        n--;
        if (Size[pu] < Size[pv]) {
            swap(pu, pv);
        }
        Size[pu] += Size[pv];
        Parent[pv] = pu;
        return true;
    }

    bool isConnected() {
        return n == 1;
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < edges.size(); ++i) {
            edges[i].push_back(i);
        }

        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });

        auto findMST = [&](int index, bool include) -> int {
            UnionFind uf(n);
            int wgt = 0;
            if (include) {
                wgt += edges[index][2];
                uf.unionSets(edges[index][0], edges[index][1]);
            }
            for (int i = 0; i < edges.size(); ++i) {
                if (i == index) continue;
                if (uf.unionSets(edges[i][0], edges[i][1])) {
                    wgt += edges[i][2];
                }
            }
            return uf.isConnected() ? wgt : INT_MAX;
        };

        int mst_wgt = findMST(-1, false);
        vector<int> critical, pseudo;

        for (int i = 0; i < edges.size(); ++i) {
            if (mst_wgt < findMST(i, false)) {
                critical.push_back(edges[i][3]);
            } else if (mst_wgt == findMST(i, true)) {
                pseudo.push_back(edges[i][3]);
            }
        }

        return { critical, pseudo };
    }
};