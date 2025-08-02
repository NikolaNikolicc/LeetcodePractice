class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        
        helper = [False for _ in range(len(p) + 1)]
        helper[-1] = True

        for s1 in range(len(s), -1, -1):
            row = [False for _ in range(len(p) + 1)]
            row[-1] = (s1 == len(s)) # this is needed in case s = nnn and p = n* so we need to fill last row but value at the end of the row in that case need to be True so we add this condition or we can initialize it before loop
            for p1 in range(len(p) - 1, -1, -1):
                match = s1 < len(s) and (s[s1] == p[p1] or p[p1] == ".")
                
                if p1 < len(p) - 1 and p[p1 + 1] == "*":
                    row[p1] = row[p1 + 2]
                    if match:
                        row[p1] = row[p1] or helper[p1]
                elif match:
                    row[p1] = helper[p1 + 1]

            helper = row
        return helper[0]

    def isMatchInitializationBeforeLoop(self, s: str, p: str) -> bool:
        
        row = [False for _ in range(len(p) + 1)]

        row[-1] = True
        for p1 in range(len(p) - 1, -1, -1):
            if p1 < len(p) - 1 and p[p1 + 1] == "*":
                row[p1] = row[p1 + 2]
        
        for s1 in reversed(range(len(s))):
            new = [False for _ in range(len(p) + 1)]
            for p1 in reversed(range(len(p))):

                match = s[s1] == p[p1] or p[p1] == "."
                
                if p1 < len(p) - 1 and p[p1 + 1] == "*":
                    new[p1] = new[p1 + 2]
                    if match:
                        new[p1] = new[p1] or row[p1]
                elif match:
                    new[p1] = row[p1 + 1]
            
            row = new
        return row[0]
    
    def recursion(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(s1, p1):

            if (s1, p1) in cache:
                return cache[(s1, p1)] 

            if p1 >= len(p):
                if s1 >= len(s):
                    return True
                else:
                    return False

            match = s1 < len(s) and (p[p1] == s[s1] or p[p1] == ".")

            if p1 < len(p) - 1 and p[p1 + 1] == "*":
                cache[(s1, p1)] = match and dfs(s1 + 1, p1) or dfs(s1, p1 + 2)
                return cache[(s1, p1)] 

            cache[(s1, p1)] = False
            if match:
                cache[(s1, p1)] = dfs(s1 + 1, p1 + 1)
            
            return cache[(s1, p1)] 

        return dfs(0, 0)
    
s="mississippi"
p="mis*is*p*."
sol = Solution()
sol.isMatch(s, p)