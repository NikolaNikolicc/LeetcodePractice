from typing import List

class Solution:
    def solution(self, R: List[str])->int:
        self.ROWS = len(R)
        self.COLS = len(R[0])
        
        self.dir = 0

        visited = set()
        directions = [[0, +1], [+1, 0], [0, -1], [-1, 0]]
        
        self.currLen = 0
        def dfs(r, c):

            if r < 0 or c < 0 or c >= self.COLS or r >= self.ROWS or R[r][c] == "X":
                return 0

            if (r, c) in visited:
                return -1

            self.currLen += 1
            visited.add((r, c))
            res = -2
            while res != -1:
                row = r + directions[self.dir][0]
                col = c + directions[self.dir][1]

                res = dfs(row, col)
                if res > 0:
                    break
                elif res == 0:
                    self.dir = (self.dir + 1) % 4
                    self.currLen = 0

            return self.currLen
                
        dfs(0, 0)
        return len(visited)

sol = Solution()
R = ["...X..", "....XX", "..X..."]
print(sol.solution(R))