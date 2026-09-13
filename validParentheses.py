# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 1 or not s.startswith(("(", "{", "[")):
            return False
        stack = []
        oposite = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in range(0, l):
            if s[i] in ("(", "{", "["):
                stack.append(s[i])
            elif not stack:
                return False
            else:
                k = stack.pop()
                if s[i] != oposite[k]:
                    return False
        return len(stack) == 0