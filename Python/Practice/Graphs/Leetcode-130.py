from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        self.ROWS, self.COLS = len(board), len(board[0])
        directions = [[-1, 0], [+1, 0], [0, +1], [0, -1]]
        
        border = set()

        def bfs(r, c):
            
            if board[r][c] == "X" or (r, c) in border:
                return
            
            q = deque()
            q.append((r, c))
            
            while q:

                for _ in range(len(q)):
                    r, c = q.popleft()

                    border.add((r, c))

                    for dir in directions:
                        nr, nc = r + dir[0], c + dir[1]
                        if min(nr, nc) >= 0 and nr < self.ROWS and nc < self.COLS and (nr, nc) not in border and board[nr][nc] == "O":
                            q.append((nr, nc))

                    
            

        for c in range(self.COLS):
            bfs(0, c)
            bfs(self.ROWS - 1, c)

        for r in range(1, self.ROWS - 1):
            bfs(r, 0)
            bfs(r, self.COLS - 1)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if (r, c) not in border:
                    board[r][c] = "X"