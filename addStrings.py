# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        rem = 0
        res = []
        l_1, l_2 = len(num1) - 1, len(num2) - 1
        while l_1 >= 0 or l_2 >= 0:
            d_1 = 0 if l_1 < 0 else int(num1[l_1])
            d_2 = 0 if l_2 < 0 else int(num2[l_2])
            s = d_1 + d_2 + rem
            res.append(str(s % 10))
            rem = s // 10
            l_1 -= 1
            l_2 -= 1
        if rem > 0:
            res.append(str(rem))
        
        return "".join(res[::-1])