class Solution {
public:

    int calc(vector<int> p1, vector<int> p2){
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        
        unordered_map<int, vector<pair<int, int>>> adj;

        for (int i = 0; i < points.size(); i++){
            for (int j = i + 1; j < points.size(); j++){
                adj[i].push_back({calc(points[i], points[j]), j});
            }
        }

        unordered_set<int> visited;
        int mst = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        
        for (auto [w1, dst]: adj[0]){
            minHeap.push({w1, dst});
        }
        visited.insert(0);

        while (!minHeap.empty() && visited.size() != points.size()){
            auto [w1, dst] = minHeap.top();
            minHeap.pop();

            if (visited.count(dst))continue;
            mst += w1;
            visited.insert(dst);

            for (auto [w2, v]: adj[dst]){
                if (visited.count(v))continue;
                minHeap.push({w2, v});
            }
        }
        return mst;
    }
};
