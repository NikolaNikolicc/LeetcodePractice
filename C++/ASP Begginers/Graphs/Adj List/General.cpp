class Graph {
private:
    unordered_map<int, vector<int>> adj;
    unordered_set<int> visit;
    
    bool dfs(int node, int target){
        if (visit.count(node)){
            return false;
        }
        
        if (node == target){
            return true;
        }

        visit.insert(node);
        for (int nei: adj[node]){
            if (dfs(nei, target)){
                return true;
            }
        }
        return false;
    }

public:
    Graph() {}

    void addEdge(int src, int dst) {
        adj[src].push_back(dst);
    }

    bool removeEdge(int src, int dst) {
        auto it = find(adj[src].begin(), adj[src].end(), dst);
        if (it != adj[src].end()){
            adj[src].erase(it);
            return true;
        }
        return false;
    }

    bool hasPath(int src, int dst) {
        visit.clear();
        return dfs(src, dst);
    }
};
