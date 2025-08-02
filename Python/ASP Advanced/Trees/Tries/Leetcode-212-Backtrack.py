from typing import List

class Solution:
    def findWordsBackTrack(self, board: List[List[str]], words: List[str]) -> List[str]:

        visited = set()
        def dfs(w, pos, r, c):
            ROWS, COLS = len(board), len(board[0])
            
            if pos == len(words[w]):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or \
            board[r][c] != words[w][pos]:
                return False

            visited.add((r, c))
            
            if words[w] == "eat":
                print(visited)
            
            res = dfs(w, pos + 1, r + 1, c) or \
                dfs(w, pos + 1, r - 1, c) or \
                dfs(w, pos + 1, r, c + 1) or \
                dfs(w, pos + 1, r, c - 1)

            visited.remove((r, c))

            return res
                    
        ROWS, COLS = len(board), len(board[0])
        output = []
        for i in range(len(words)):
            found = False
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == words[i][0]:
                        if dfs(i, 0, r, c):
                            output.append(words[i])
                            found = True
                            break
                if found:
                    break

        return output

sol = Solution()
board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words=["oath","pea","eat","rain"]
print(sol.findWords(board, words))