class Solution:
    def isValidFirst(self, s: str) -> bool:
        stack = []
        for elem in s:
            if elem in ("(", "{", "["):
                stack.append(elem)
            elif len(stack) == 0:
                return False
            elif elem == ")":
                if stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            elif elem == "}":
                if stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            elif elem == "]":
                if stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
        return True if len(stack) == 0 else False
             
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}    

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False