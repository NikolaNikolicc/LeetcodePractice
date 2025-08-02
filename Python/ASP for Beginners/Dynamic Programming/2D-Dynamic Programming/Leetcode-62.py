class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        oldRow = [1]*n
        for r in range(m - 2, -1, -1):
            newRow = [0]*n
            newRow[-1] = 1
            for c in range(n - 2, -1, -1):
                newRow[c] = newRow[c + 1] + oldRow[c]
            oldRow = newRow[:]
        return oldRow[0]