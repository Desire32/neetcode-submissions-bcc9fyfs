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
            elif stack[-1] == brackets[ch] and stack:
                stack.pop()
            else:
                return False
        return True
        