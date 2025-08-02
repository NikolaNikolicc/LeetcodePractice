#include <vector>
#include <utility>

using namespace std;

class Solution {
private:
    int maxArea = 0;
    int area;
    int ROWS;
    int COLS;
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    void dfs(int r, int c, vector<vector<int>>& grid){
        if (min(r, c) < 0 || r >= ROWS || c >= COLS || !grid[r][c]){
            return;
        }

        area++;
        grid[r][c] = 0;
        for (pair<int, int> dir: directions){
            dfs(r + dir.first, c + dir.second, grid);
        }
    }
    
    
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == 1){
                    area = 0;
                    dfs(r, c, grid);                  
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
};