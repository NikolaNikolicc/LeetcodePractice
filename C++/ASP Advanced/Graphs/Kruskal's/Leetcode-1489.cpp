class UnionFind {
private:
    unordered_map<int, int> parent;
    unordered_map<int, int> rank;
    int maxRank = 0;
public:
    UnionFind(int n){
        for (int i = 0; i < n; i++){
            rank[i] = 1;
            parent[i] = i;
        }
        maxRank = 1;
    }

    int find(int x){
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // path compression
        }
        return parent[x];
    }

    bool union_(int x, int y){
        int parx = find(x), pary = find(y);
        if (parx == pary) return false;

        if (rank[parx] > rank[pary]){
            parent[pary] = parx;
            rank[parx] += rank[pary];
            maxRank = max(maxRank, rank[parx]);
        } else {
            parent[parx] = pary;
            rank[pary] += rank[parx];
            maxRank = max(maxRank, rank[pary]);
        }
        return true;
    }

    int getMaxRank() { return maxRank; }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        int m = edges.size();
        for (int i = 0; i < m; i++) {
            edges[i].push_back(i); // store original index
        }

        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });

        // build base MST
        UnionFind baseUF(n);
        int mst = 0;
        for (const vector<int>& edge : edges) {
            int a = edge[0], b = edge[1], w = edge[2];
            if (baseUF.union_(a, b)) {
                mst += w;
            }
        }

        unordered_set<int> critical;
        for (int i = 0; i < m; i++) {
            UnionFind uf(n);
            int mmst = 0;
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                const vector<int>& edge = edges[j];
                int a = edge[0], b = edge[1], w = edge[2];
                if (uf.union_(a, b)) {
                    mmst += w;
                }
            }
            // if we can't form MST or the cost is larger, edge is critical
            int sets = uf.getMaxRank();
            if (sets != n || mmst > mst) {
                critical.insert(edges[i][3]);
            }
        }

        vector<int> pseudo_critical;
        for (int i = 0; i < m; i++) {
            UnionFind uf(n);
            int mmst = 0;
            const vector<int>& edge = edges[i];
            int a = edge[0], b = edge[1], w = edge[2], idx = edge[3];
            uf.union_(a, b);
            mmst += w;

            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                const vector<int>& e = edges[j];
                if (uf.union_(e[0], e[1])) {
                    mmst += e[2];
                }
            }

            int sets = uf.getMaxRank();
            if (mmst == mst && sets == n && !critical.count(idx)) {
                pseudo_critical.push_back(idx);
            }
        }

        return {
            vector<int>(critical.begin(), critical.end()),
            pseudo_critical
        };
    }
};
