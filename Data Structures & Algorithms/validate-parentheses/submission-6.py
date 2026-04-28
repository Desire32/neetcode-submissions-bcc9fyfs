class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            if stack[-1] == brackets[ch]:
                stack.pop()
            else:
                return False
        return True
        