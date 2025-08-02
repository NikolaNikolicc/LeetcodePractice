class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        codeBook = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        curr = []
        def dfs(pos):

            if pos == len(digits):
                res.append("".join(curr))
                return

            letters = codeBook[digits[pos]]

            for letter in letters:
                curr.append(letter)
                dfs(pos + 1)
                curr.pop()


        dfs(0)
        return res if len(digits) > 0 else []