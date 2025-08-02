from typing import List

class Solution:
    def solveNQueensHashing(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
    
    def solveNQueensClassicalBacktrack(self, n: int) -> List[List[str]]:
        def isSafe(r, c):                
            for i in range(r):
                if board[i][c] == "Q":
                    return False
            
            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = r, c
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True
        

        board = [["." for i in range(n)] for i in range(n)]
        output = []

        def backtrack(r):
            if r == n:
                output.append(["".join(elem) for elem in board])
                return

            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return output


sol = Solution()
print(sol.solveNQueens(4))