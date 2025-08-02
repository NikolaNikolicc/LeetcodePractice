class UnionFind {
private:
    unordered_map<int, int> parent;
    unordered_map<int, int> rank;
    int numComponents;
public:
    UnionFind(int n) {
        for (int i = 0; i < n; i++){
            parent[i] = i;
            rank[i] = 1;
        }
        numComponents = n;
    }

    int find(int x) {
        int curr = x;
        while (parent[curr] != curr){
            parent[curr] = parent[parent[curr]];
            curr = parent[curr];
        }
        return curr;
    }

    bool isSameComponent(int x, int y) {
        return find(x) == find(y);
    }

    // Union is a reserved keyword in C++, so we use _union instead
    bool _union(int x, int y) {
        int parx = find(x), pary = find(y);
        if (parx == pary)return false;
        if (rank[parx] > rank[pary]){
            parent[pary] = parx;
        } else if (rank[parx] < rank[pary]){
            parent[parx] = pary;
        } else {
            parent[parx] = pary;
            rank[pary]++;
        }
        numComponents--;
        return true;
    }

    int getNumComponents() {
        return numComponents;
    }
};
// The code implements a Union-Find (Disjoint Set Union) data structure in C++. It provides methods to find the root of a component, check if two elements are in the same component, perform union operations, and retrieve the number of components. The implementation uses path compression for efficient find operations and union by rank to keep the tree flat, ensuring optimal performance for union and find operations. This structure is useful for problems involving connectivity in graphs or sets.