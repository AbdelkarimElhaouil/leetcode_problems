# 3498. Reverse Degree of a String

class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord("z") - ord(s[i]) + 1) * (i + 1) for i in range(len(s)))
