from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        minHeap = [(grid[0][0], 0, 0)]

        path = {}
        ret = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while (ROWS - 1, COLS - 1) not in path:

            w, r, c = heapq.heappop(minHeap)

            if (r, c) in path:
                continue
            
            # print("(" + str(r) + ", " + str(c) + ")")

            if w > ret:
                ret = w
            
            path[(r, c)] = ret


            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in path:
                    continue

                heapq.heappush(minHeap, (grid[nr][nc], nr, nc))

        return path[(ROWS - 1, COLS - 1)]

sol = Solution()
grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]
]

print(sol.swimInWater(grid))