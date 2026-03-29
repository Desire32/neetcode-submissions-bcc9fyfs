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
            elif ch in brackets.keys():
                if not stack or stack[-1] != brackets[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
        