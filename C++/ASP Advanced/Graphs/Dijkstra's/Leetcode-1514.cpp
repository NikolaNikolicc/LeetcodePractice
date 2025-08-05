class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        unordered_map<int, vector<pair<double,int>>> adj;

        for (int i = 0; i < edges.size(); i++){
            vector<int> edge = edges[i];
            int a = edge[0], b = edge[1];
            double sp = succProb[i];
            adj[a].push_back({sp, b});
            adj[b].push_back({sp, a});
        }

        priority_queue<pair<double, int>> maxHeap;
        maxHeap.push({1, start_node});

        unordered_map<int, double> shortest;

        while (!maxHeap.empty()){
            auto [p1, src] = maxHeap.top();
            maxHeap.pop();

            if (shortest.count(src))continue;
            if (src == end_node)return p1;
            shortest[src] = p1;

            for (auto [p2, dst]: adj[src]){
                if (shortest.count(dst))continue;
                maxHeap.push({p1 * p2, dst});
            }
        }
        return 0;
    }
};