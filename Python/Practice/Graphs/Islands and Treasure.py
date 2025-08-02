from typing import List
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.INF = 2147483647

        q = collections.deque()
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
        visited = set()
        while q:

            for _ in range(len(q)):
                print(q)
                r, c = q.popleft()
                visited.add((r, c))
                for dir in directions:
                    nr, nc = r + dir[0], c + dir[1]
                    if min(nr, nc) >= 0 and nr < self.ROWS and nc < self.COLS and \
                        (nr, nc) not in visited and grid[nr][nc] == self.INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))

            

sol = Solution()
grid=[[0,-1],[2147483647,2147483647]]
sol.islandsAndTreasure(grid)