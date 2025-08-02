class Solution:
    def longestCommonSubsequenceDFSWithCache(self, text1: str, text2: str) -> int:
        
        cache = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]
        return dfs(0, 0)

    def longestCommonSubsequenceBottomUp(self, text1: str, text2: str) -> int:
        # swap strings if needed so we have longner text in text2
        if len(text1) > len(text2):
            text1, text2 = text2, text1
            
        oldRow = [0]*(len(text1) + 1)
        newRow = [0]*(len(text1) + 1)
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text2[r] == text1[c]:
                    newRow[c] = 1 + oldRow[c + 1]
                else:
                    newRow[c] = max(oldRow[c], newRow[c + 1])

            oldRow = newRow[:]

        return newRow[0]

    def longestCommonSubsequenceSpaceOptimized(self, text1: str, text2: str) -> int:
        # swap strings if needed so we have longner text in text2
        if len(text1) > len(text2):
            text1, text2 = text2, text1
            
        oldRow = [0]*(len(text1) + 1)
        
        for r in range(len(text2) - 1, -1, -1):
            # Previous value is used so we maintain old value in case string2 has two same characters in a row
            # In that case we want to increment value in list only once 
            prev = 0
            for c in range(len(text1) - 1, -1, -1):
                tmp = oldRow[c]
                if text2[r] == text1[c]:
                    oldRow[c] = 1 + prev
                else:
                    oldRow[c] = max(oldRow[c], oldRow[c + 1])

                prev = tmp
            

        return oldRow[0]