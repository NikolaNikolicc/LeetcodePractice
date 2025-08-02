class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.index = -1

    def addWord(self, word, index):
        curr = self
        for ch in word:
            c = ord(ch) - ord("a")
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.index = index

    def searchWord(self, word):
        curr = self
        for ch in word:
            c = ord(ch) - ord("a")
            if not curr.children[c]:
                return -1
            curr = curr.children[c]
        return curr.index

class WordFilter(object):

    def __init__(self, words):
        self.root = TrieNode()
        self.CHAR = str(chr(ord("z") + 1))

        # this is char '{', we want first next char after 'z' so we can store it in array children
        # by simply calculating ord(ch) - ord('a')

        for index in range(len(words)):
            w = words[index]
            for i in range(len(w)):
                suff = w[i:]
                for j in range(len(w) + 1):
                    pref = w[:j]
                    self.root.addWord(pref + self.CHAR + suff, index)


        

    def f(self, pref, suff):
        return self.root.searchWord(pref + self.CHAR + suff)


# time limit exceeded :(