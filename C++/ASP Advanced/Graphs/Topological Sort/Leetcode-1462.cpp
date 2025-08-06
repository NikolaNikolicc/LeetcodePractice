class Solution {
    vector<vector<int>> adj;
    unordered_map<int, unordered_set<int>> prereqMap;

    void topo(int node){

        if (prereqMap.count(node)){
            return;
        }

        for (auto nei: adj[node]){
            topo(nei);
            prereqMap[node].insert(prereqMap[nei].begin(), prereqMap[nei].end());
        }
        prereqMap[node].insert(node);
    }

public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        adj.assign(numCourses, vector<int>());
        for (vector<int>& pre: prerequisites){
            adj[pre[1]].push_back(pre[0]);
        }

        for (int i = 0; i < numCourses; i++){
            topo(i);
        }

        vector<bool> res;

        for (auto& query: queries){
            res.push_back(prereqMap[query[1]].count(query[0]));
        }
        
        return res;
    }
};