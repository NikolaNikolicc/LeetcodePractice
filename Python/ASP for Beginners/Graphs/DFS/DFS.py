class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        visited = set()
        def dfs(r, c):

            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or (r, c) in visited or r >= ROWS or c >= COLS or grid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            cnt = 0

            visited.add((r, c))

            cnt += dfs(r + 1, c)
            cnt += dfs(r - 1, c)
            cnt += dfs(r, c + 1)
            cnt += dfs(r, c - 1)

            visited.remove((r, c))

            return cnt

        return dfs(0, 0)
