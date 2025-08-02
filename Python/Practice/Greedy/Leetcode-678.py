class Solution:
    def checkValidString(self, s: str) -> bool:
        openParenIndex = []
        starIndex = []

        for i, elem in enumerate(s):
            if elem == "(":
                openParenIndex.append(i)
            elif elem == "*":
                starIndex.append(i)
            else:
                if len(openParenIndex) > 0:
                    openParenIndex.pop()
                elif len(starIndex) > 0:
                    starIndex.pop()
                else:
                    return False

        starNum = 0
        for paren in openParenIndex:
            while starNum < len(starIndex) and starIndex[starNum] < paren:
                starNum += 1

            if starNum == len(starIndex):
                return False

            starNum += 1
        return True
                