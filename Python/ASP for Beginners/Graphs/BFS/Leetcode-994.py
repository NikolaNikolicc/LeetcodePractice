# https://leetcode.com/problems/rotting-oranges/description/

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        steps = [[+1, 0], [-1, 0], [0, +1], [0, -1]]

        rotten = deque()
        fresh = 0

        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while rotten:
            print("time: " + str(time))
            print(rotten)
            hasNext = 0
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for rr, cc in steps:
                    if min(r + rr, c + cc) < 0 or r + rr >= ROWS or c + cc >= COLS or \
                    grid[r + rr][c + cc] == 2 or grid[r + rr][c + cc] == 0:    
                        continue

                    hasNext += 1    
                    rotten.append((r + rr, c + cc))
                    grid[r + rr][c + cc] = 2
                    fresh -= 1

            if hasNext > 0:
                time += 1

        return time if fresh == 0 else -1



sol = Solution()
grid=[[1,1,0],[0,1,1],[0,1,2]]
print(sol.orangesRotting(grid))