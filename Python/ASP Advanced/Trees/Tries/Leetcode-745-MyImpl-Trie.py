class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []

    def addWord(self, word, index):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.indices.append(index)

class WordFilter(object):

    def __init__(self, words):
        self.rootPref = TrieNode()
        self.rootSuf = TrieNode()
        for i in range(len(words)):
            w = words[i]
            self.rootPref.addWord(w, i)
            self.rootSuf.addWord(w[::-1], i)

        

    def f(self, pref, suff):
        curr = self.rootPref
        for c in pref:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return -1

        indicesPrefix = curr.indices

        curr = self.rootSuf
        for c in suff[::-1]:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return -1

        indicesSufix = curr.indices

        intersection = list(set(indicesPrefix) & set(indicesSufix))

        return max(intersection) if len(intersection) > 0 else -1

# time limit exceeded :(