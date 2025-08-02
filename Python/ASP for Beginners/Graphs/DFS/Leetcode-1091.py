from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit = set()
        q = deque()
        if grid[0][0] == 1:
            return -1
            
        q.append((0,0)) 
        visit.add((0,0))

        ROWS, COLS = len(grid), len(grid[0])
        steps = [[-1, 0], [-1, +1], [0, +1], [+1, +1], [+1, 0], [+1, -1], [0, -1], [-1, -1]]

        length = 1
        while q:
            for i in range(len(q)):
                
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for rr, cc in steps:
                    if min(r + rr, c + cc) < 0 or r + rr >= ROWS or c + cc >= COLS \
                    or (r + rr, c + cc) in visit or grid[r + rr][c + cc] == 1:
                        continue

                    q.append((r + rr, c + cc))
                    visit.add((r + rr, c + cc))

            length += 1
        return -1