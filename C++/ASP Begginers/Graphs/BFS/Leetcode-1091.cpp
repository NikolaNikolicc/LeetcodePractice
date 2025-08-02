class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int N = grid.size();

        vector<vector<bool>> visited(N, vector<bool>(N, false));
        queue<pair<int, int>> q;
        if (!grid[0][0]){
            q.push({0, 0});
        }

        vector<vector<int>> neighbors = {{-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}};
        int path = 1;
        while (!q.empty()){
            int size = q.size();
            for (int i = 0; i < size; i++){
                pair<int, int> elem = q.front();
                q.pop();
                int r = elem.first, c = elem.second;
                
                if (r == N - 1 && c == N - 1){
                    return path;
                }

                for (vector<int> nei: neighbors){
                    int newR = r + nei[0], newC = c + nei[1];

                    if (min(newR, newC) < 0 || newR >= N || newC >= N || grid[newR][newC] == 1 || visited[newR][newC]){
                        continue;
                    }

                    q.push({newR, newC});
                }
                visited[r][c] = true;

            }
            path++;
        }
        return -1;
    }
};