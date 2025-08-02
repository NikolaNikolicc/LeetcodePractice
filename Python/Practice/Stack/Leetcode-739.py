class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1], len(temperatures) - 1)]
        res = [0]
        for i in range(len(temperatures) - 2, -1, -1):

            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)

            stack.append([temperatures[i], i])

        return res[::-1]