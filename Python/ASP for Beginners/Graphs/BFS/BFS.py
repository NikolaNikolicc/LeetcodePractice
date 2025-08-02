class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        q.append((0,0))
        visit.add((0,0))
        steps = [[+1,0], [-1,0], [0,+1], [0,-1]]
        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for step in steps:
                    rr, cc = step[0], step[1]
                    if min(r + rr, c + cc) < 0 or r + rr >= ROWS or c + cc >= COLS \
                    or (r + rr, c + cc) in visit or grid[r + rr][c + cc] == 1:
                        continue

                    q.append((r + rr, c + cc))
                    visit.add((r + rr, c + cc))
            length += 1
        return -1