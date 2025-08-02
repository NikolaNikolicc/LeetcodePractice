from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 + elem2)
            elif token == "-":
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 - elem2)
            elif token == "*":
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 * elem2)
            elif token == "/":
                elem2 = stack.pop()
                elem1 = stack.pop()
                # Koristimo int(elem1/elem2) za truncation prema nuli
                stack.append(int(elem1 / elem2))
            else:
                stack.append(int(token))
        return stack[0]
