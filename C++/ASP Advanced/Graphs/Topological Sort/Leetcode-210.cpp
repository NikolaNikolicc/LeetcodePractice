class Solution {
private:
    unordered_map<int, vector<int>> adj;
    unordered_set<int> path;
    unordered_set<int> visited;

    vector<int> topoSort;
    
    bool topo(int node){
        if (path.count(node)) return true;
        if (visited.count(node)) return false;

        path.insert(node);
        for (auto nei: adj[node]){
            if (topo(nei)){
                return true;
            }
        }
        path.erase(node);
        visited.insert(node);
        topoSort.push_back(node);
        return false;
    }
    
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (auto pre: prerequisites){
            int src = pre[1], dst = pre[0];
            adj[src].push_back(dst);
        }

        for (int i = 0; i < numCourses; i++){
            if (topo(i)){
                return vector<int>();
            }
        }

        reverse(topoSort.begin(), topoSort.end());
        return topoSort;
    }
};
