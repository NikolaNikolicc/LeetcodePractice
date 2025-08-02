from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        self.ROWS, self.COLS = len(heights), len(heights[0])
        
        a, p = set(), set()

        # for i in range(self.ROWS):
        #     a.add((i, 0))
        #     p.add((i, self.COLS - 1))

        # for i in range(self.COLS):
        #     a.add((0, i))
        #     p.add((self.ROWS - 1, i))

        directions = [[+1, 0], [-1, 0], [0, +1], [0, -1]]

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= self.ROWS or c >= self.COLS or (r, c) in visit or \
            heights[r][c] < prevHeight:
                return

            visit.add((r, c))
            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                dfs(row, col, visit, heights[r][c])

        for i in range(self.ROWS):
            dfs(i, 0, a, heights[i][0])
            dfs(i, self.COLS - 1, p, heights[i][self.COLS - 1])

        print(a)
        print(p)
        for i in range(self.COLS):
            dfs(0, i, a, heights[0][i])
            dfs(self.ROWS - 1, i, p, heights[self.ROWS - 1][i])

        res = []
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if (r, c) in a and (r, c) in p:
                    res.append([r, c])
        return res

sol = Solution()
heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
print(sol.pacificAtlantic(heights))