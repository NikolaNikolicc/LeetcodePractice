class Solution {
private:
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int ROWS;
    int COLS;
public:
    void dfs(vector<vector<char>>& grid, int r, int c){
        if (min(r, c) < 0 || r >= ROWS || c >= COLS || grid[r][c] == '0'){
            return;
        }

        grid[r][c] = '0';
        for (pair<int, int> dir: directions){
            dfs(grid, r + dir.first, c + dir.second);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int cnt = 0;
        ROWS = grid.size();
        COLS = grid[0].size();
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == '1'){
                    dfs(grid, r, c);
                    cnt++;
                }
            }
        }
        return cnt;
    }
};
