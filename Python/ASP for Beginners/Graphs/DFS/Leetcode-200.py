# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        
        visited = []
        for row in grid:
            visited.append([False] * len(row))

        numOfIslands = 0

        def dfs(r, c):

            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or visited[r][c]:
                return

            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    numOfIslands += 1

        return numOfIslands