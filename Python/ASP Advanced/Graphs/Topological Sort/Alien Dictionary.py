from typing import List
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {character:[] for word in words for character in word}
        
        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                i += 1

            if i < len(word1) and i < len(word2):
                adj[word1[i]].append(word2[i])  # Add edge
            elif len(word1) > len(word2):  # Invalid case (e.g., "abc" before "ab")
                return False  # Indicate invalid order
            return True
        
        for i in range(1, len(words)):
            if not compare(words[i - 1], words[i]):
                return ""

        visited = set()
        path = set()
        final = []

        def topoSort(i):

            if i in path:
                return False

            if i in visited:
                return True

            path.add(i)
            for nei in adj[i]:
                if not topoSort(nei):
                    return False
            path.remove(i)

            final.append(i)
            visited.add(i)
            return True

        for i in adj:
            if not topoSort(i):
                return ""
        return "".join(final[::-1])

        


words = ["hrn","hrf","er","enn","rfnn"]
sol = Solution()
print(sol.foreignDictionary(words))