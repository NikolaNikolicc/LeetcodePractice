#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
private:
    unordered_map<int, vector<int>> adj;
    unordered_set<int> visited;

    bool dfs(int i){


        if (visited.count(i)){
            return false;
        }

        if (!adj.count(i)){
            return true;
        }

        visited.insert(i);
        for (int nei: adj[i]){
            if (!dfs(nei)){
                return false;
            }
        }
        visited.erase(i);
        adj[i].clear();

        return true;

    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (vector<int> pre: prerequisites){
            int a = pre[0], b = pre[1];
            adj[b].push_back(a);
        }

        for (int i = 0; i < numCourses; i++){
            if (!dfs(i)){
                return false;
            }
        }

        return true;

    }
};
