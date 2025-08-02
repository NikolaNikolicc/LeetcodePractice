# https://leetcode.com/problems/max-area-of-island/description/

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIslandDFS(self, grid: List[List[int]]) -> int:
        
        visited = []

        for list in grid:
            visited.append([False]*len(list))

        maxSize = 0

        def dfs(r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or visited[r][c]:
                return 0

            visited[r][c] = True

            size = 1

            size += dfs(r - 1, c)
            size += dfs(r + 1, c)
            size += dfs(r, c + 1)
            size += dfs(r, c - 1)

            return size


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    # currSize[0] = 0
                    currSize = dfs(r, c)
                    maxSize = max(maxSize, currSize)

        return maxSize

    def maxAreaOfIslandBFS(self, grid: List[List[int]]) -> int:
        
        visited = []

        for list in grid:
            visited.append([False]*len(list))

        maxSize = 0

        def bfs(r, c):

            ROWS, COLS = len(grid), len(grid[0])
            steps = [(-1, 0), (+1, 0), (0, +1), (0, -1)]

            q = deque()
            q.append((r, c))

            size = 0

            while len(q) > 0:
                rr, cc = q.popleft()
                if not visited[rr][cc]:
                    size += 1
                visited[rr][cc] = True
                print(str(rr) + " " + str(cc), end="; ")
                for step in steps:
                    if rr + step[0] >= 0 and rr + step[0] < ROWS \
                    and cc + step[1] >= 0 and cc + step[1] < COLS \
                    and not visited[rr + step[0]][cc + step[1]] \
                    and grid[rr + step[0]][cc + step[1]] == 1:
                        q.append((rr + step[0], cc + step[1]))

            return size



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    # currSize[0] = 0
                    currSize = bfs(r, c)
                    maxSize = max(maxSize, currSize)

        return maxSize


sol = Solution()
print(sol.maxAreaOfIsland([[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]))