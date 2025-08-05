class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        
        auto lambda = [](const vector<int>& a,const vector<int>& b){
            return a[0] > b[0];
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(lambda)> minHeap(lambda);

        minHeap.push({grid[0][0], 0, 0});
        int time = 0;

        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        int ROWS = grid.size(), COLS = grid[0].size();

        while (true){
            vector<int> elem = minHeap.top();
            int len = elem[0], r = elem[1], c = elem[2];
            minHeap.pop();
            time = max(time, elem[0]);
            grid[r][c] = -1;

            if (r == ROWS - 1 && c == COLS - 1)return time;

            for (pair<int, int> dir: dirs){
                int nr = r + dir.first, nc = c + dir.second;

                if (min(nr, nc) < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == -1)continue;
                minHeap.push({grid[nr][nc], nr, nc});

            }
        }
    }
};

class SolutionNeet {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int N = grid.size();
        set<pair<int, int>> visit;
        priority_queue<vector<int>,
                       vector<vector<int>>, greater<>> minHeap;
        vector<vector<int>> directions = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };

        minHeap.push({grid[0][0], 0, 0});
        visit.insert({0, 0});

        while (!minHeap.empty()) {
            auto curr = minHeap.top();
            minHeap.pop();
            int t = curr[0], r = curr[1], c = curr[2];
            if (r == N - 1 && c == N - 1) {
                return t;
            }
            for (const auto& dir : directions) {
                int neiR = r + dir[0], neiC = c + dir[1];
                if (neiR < 0 || neiC < 0 || neiR == N ||
                    neiC == N || visit.count({neiR, neiC})) {
                    continue;
                }
                visit.insert({neiR, neiC});
                minHeap.push({
                    max(t, grid[neiR][neiC]), neiR, neiC
                });
            }
        }

        return N * N;
    }
};