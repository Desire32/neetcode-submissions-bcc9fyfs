class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for ch in s:
            stack.append(ch)
        for el in stack:
            while el in brackets:
                stack.pop()
            return True
        return False