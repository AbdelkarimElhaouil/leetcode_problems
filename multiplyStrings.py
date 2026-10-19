from collections import deque

class Solution:
    def addStr(num1: str, num2: str) -> str:
        pass
    
    def multiply(self, num1: str, num2: str) -> str:
        l_1, l_2 = len(num1), len(num2)
        res = "0"
        zero_ascii = ord('0')
        for i in range(l_1 - 1, -1, -1):
            rem = 0 
            tmp_res = deque()
            d_1 = ord(num1[i]) - zero_ascii
            # if d_1 == 0:
            for j in range(l_2 - 1, -1, -1):
                d_2 = ord(num2[j]) - zero_ascii
                s = d_1 * d_2 + rem
                tmp_res.appendleft(chr(s % 10 + zero_ascii))
            if rem > 0:
                tmp_res.appendleft(chr(rem + zero_ascii))

            res = self.addStr()


# for i in range(5 - 1, -1, -1):
#     print(i)
