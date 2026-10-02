# 2351. First Letter to Appear Twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique = set()
        for i in range(len(s)):
            if s[i] in unique:
                return s[i]
            unique.add(s[i])