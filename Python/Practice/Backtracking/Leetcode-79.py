class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() 
        
        def dfs(r, c, pos):

            if pos == len(word):
                return True
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] != word[pos]:
                return False

            visited.add((r, c))

            res = False
            for d in directions:
                row = r + d[0]
                col = c + d[1]
                res = res or dfs(row, col, pos + 1)

            visited.remove((r, c))

            return res
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False