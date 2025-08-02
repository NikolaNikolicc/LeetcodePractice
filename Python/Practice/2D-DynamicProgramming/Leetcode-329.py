class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        visited = {}

        directions = [[-1, 0], [+1, 0], [0, +1], [0, -1]]
        def dfs(r, c, prev):

            if min(r, c) < 0 or r >= self.ROWS or c >= self.COLS or prev >= matrix[r][c]:
                return 0

            if (r, c) in visited:
                return visited[(r, c)]

            ret = 0
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                ret = max(ret, dfs(nr, nc, matrix[r][c]))

            visited[(r, c)] = ret + 1
            return visited[(r, c)]            

        for r in range(self.ROWS):
            for c in range(self.COLS):
                dfs(r, c, float("-inf"))

        return max(visited.values())