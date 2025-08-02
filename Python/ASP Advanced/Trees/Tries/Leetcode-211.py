class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word):
        
        def dfs(root, position):
            curr = root

            for i in range(position, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                elif c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
            return curr.word

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)