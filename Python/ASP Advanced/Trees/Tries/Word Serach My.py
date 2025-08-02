from typing import List

class Node:
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()    
            curr = curr.child[c]

        curr.word = True
                
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.ROWS, self.COLS = len(board), len(board[0])

        trie = WordDictionary()
        for word in words:
            trie.addWord(word)

        visited = set()
        # word = ""
        res = []

        directions = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
        
        def backtrack(trieNode: Node, r: int, c: int, w: str) -> None:
            
            visited.add((r, c))
            w += board[r][c]

            if trieNode.word and w not in res:
                res.append(w[:])

            for dir in directions:
                nr, nc = r  + dir[0], c + dir[1]

                if min(nr, nc) >= 0 and nr < self.ROWS and nc < self.COLS and (nr, nc) not in visited and \
                      board[nr][nc] in trieNode.child:
                    backtrack(trieNode.child[board[nr][nc]], nr, nc, w) 
                    
            visited.remove((r, c))

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] in trie.root.child:
                    backtrack(trie.root.child[board[r][c]], r, c, "")
        
        return res
    
sol = Solution()
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
print(sol.findWords(board, words))