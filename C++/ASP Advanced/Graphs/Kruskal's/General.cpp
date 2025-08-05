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
        int curr = x;
        while (parent[curr] != curr){
            parent[curr] = parent[parent[curr]];
            curr = parent[curr];
        }
        return curr;
    }

    bool union_(int x, int y){
        int parx = find(x), pary = find(y);

        if (parx == pary)return false;

        if (rank[parx] > rank[pary]){
            parent[pary] = parx;
            rank[parx] += rank[pary];
            maxRank = max(maxRank, rank[parx]);
        } else if (rank[pary] > rank[parx]){
            parent[parx] = pary;
            rank[pary] += rank[parx];
            maxRank = max(maxRank, rank[pary]);
        } else {
            parent[pary] = parx;
            rank[parx] += rank[pary];
            maxRank = max(maxRank, rank[parx]);
        }
        
        return true;
    }

    int getMaxRank(){return maxRank;}
};

class Solution {
public:
    int minimumSpanningTree(vector<vector<int>>& edges, int n) {
        UnionFind* uf = new UnionFind(n);
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
        for (vector<int> edge: edges){
            int w = edge[2], u = edge[0], v = edge[1];
            minHeap.push({w, u, v});
        }

        int mst = 0;
        while (!minHeap.empty() && uf->getMaxRank() != n){
            auto [w, src, dst] = minHeap.top();
            minHeap.pop();

            if (uf->union_(src, dst)){
                mst += w;
            }

        }
        return (uf->getMaxRank() != n) ? -1 : mst;
    }
};


// we also could count the number of components
class UnionFindNeet {
public:
    vector<int> parent;
    vector<int> size;
    int numComponents;

    UnionFind(int n) {
        parent.resize(n);
        size.resize(n, 1);
        numComponents = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        // Finds the root of x
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union is a reserved keyword in C++, so we use _union instead
    bool _union(int x, int y) {
        // Connects x and y
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (size[rootX] < size[rootY]) {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            } else {
                parent[rootY] = rootX;
                size[rootX] += size[rootY];
            }
            numComponents--;
            return true;
        }
        return false;
    }

    int getNumComponents() {
        return numComponents;
    }
};

class SolutionNeet {
public:
    // Implementation for Kruskal's algorithm to compute Minimum Spanning Trees
    int minimumSpanningTree(vector<vector<int>>& edges, int n) {
        // Sort edges by weight using min heap
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap; 
        for (const auto& edge : edges) {
            minHeap.push(make_tuple(edge[2], edge[0], edge[1]));
        }

        UnionFind unionFind(n);
        int totalWeight = 0;
        while (!minHeap.empty()) {
            tuple<int, int, int> cur = minHeap.top();
            int w1 = std::get<0>(cur), n1 = std::get<1>(cur), n2 = std::get<2>(cur);
            minHeap.pop();

            if (unionFind._union(n1, n2)) {
                totalWeight += w1;
            }
        }
        // Return -1 if not all nodes are visited (unconnected graph)
        return unionFind.getNumComponents() != 1 ? -1 : totalWeight;
    }
};
