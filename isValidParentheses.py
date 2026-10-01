# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        stack = []
        for i in range(l):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == ')' and stack[-1] != "(":
                return False
            elif s[i] == ']' and stack[-1] != "[":
                return False
            elif s[i] == '}' and stack[-1] != "{":
                return False
            else:
                stack.pop()
        
        return not stack