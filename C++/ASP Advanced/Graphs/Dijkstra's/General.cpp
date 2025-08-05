class Solution {
public:
    unordered_map<int, int> shortestPath(int n, vector<vector<int>>& edges, int src) {
        unordered_map<int, vector<pair<int, int>>> adj; // src, {w, dst}

        // set adj
        for (auto& edge: edges){
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            adj[u].push_back({w, v});
        }

        // set shortest path
        unordered_map<int, int> shortest;
        for (int i = 0; i < n; i++){
            shortest[i] = -1;
        }

        // set min heap
        auto l = [](const pair<int, int> a,const pair<int, int> b){
            return a.first > b.first;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(l)> heap(l);
        
        // algo
        heap.push({0, src});
        while (!heap.empty()){
            auto [w1, u] = heap.top();
            heap.pop();

            if (shortest[u] != -1)continue;
            shortest[u] = w1;

            for(auto& [w2, v]: adj[u]){
                if (shortest[v] != -1)continue;
                heap.push({w1 + w2, v});
            }

        }

        return shortest;
    }
};
