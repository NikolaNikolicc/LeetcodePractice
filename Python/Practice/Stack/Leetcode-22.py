class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(num, opened, closed):
            
            if opened < closed:
                return
            
            if num == 0 and opened == closed:
                res.append("".join(stack))
                return

            if num > 0:
                stack.append("(")
                dfs(num - 1, opened + 1, closed)
                stack.pop()

            if opened > closed:
                stack.append(")")
                dfs(num, opened, closed + 1)
                stack.pop()

        dfs(n, 0, 0)
        return res