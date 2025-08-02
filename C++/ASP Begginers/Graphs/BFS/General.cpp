class Solution {
public:
    int shortestPath(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();

        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        queue<vector<int>> q;

        if (!grid[0][0]){
            q.push({0, 0});
        }

        int minLen = 0;
        
        while (!q.empty()){
            int size = q.size();
            for (int i = 0; i < size; i++){
                int r = q.front()[0], c = q.front()[1];

                q.pop();

                if (r == ROWS - 1 && c == COLS - 1){
                    return minLen;
                }

                int neighbors[4][2] = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}};

                for (int j = 0; j < 4; j++){
                    int rnei = neighbors[j][0], cnei = neighbors[j][1];

                    if (min(rnei, cnei) < 0 || rnei >= ROWS || cnei >= COLS || grid[rnei][cnei] || visited[r][c]){
                        continue;
                    }
                    q.push({rnei, cnei});
                }
                visited[r][c] = true;
            }
            minLen++;
        }

        return -1;
    }
};
