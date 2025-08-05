class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> adj;

        for (auto time: times){
            int u = time[0], v = time[1], t = time[2];
            adj[u].push_back({t, v});
        }

        unordered_map<int, int> shortest;
        int minTime = INT_MIN;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        minHeap.push({0, k});

        while (!minHeap.empty() && shortest.size() != n){
            auto [t1, dst] = minHeap.top();
            minHeap.pop();

            if (shortest.count(dst))continue;
            shortest[dst] = t1;
            minTime = max(t1, minTime);

            for (auto [t2, v]: adj[dst]){
                if (shortest.count(v))continue;

                minHeap.push({t1 + t2, v});
            }


        }

        return (shortest.size() == n) ? minTime : -1;
    }
};
