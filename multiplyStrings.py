# 43. Multiply Strings

from collections import deque

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        l_1, l_2 = len(num1), len(num2)
        result = deque()
        zero_ascii = ord('0')
        for i in range(l_1):
            rem = 0
            res_len = len(result)
            d_1 = ord(num1[l_1 - i - 1]) - zero_ascii
            for j in range(l_2):
                d_2 = ord(num2[l_2 - j - 1]) - zero_ascii
                s = d_1 * d_2 + rem
                if i + j < res_len:
                    s += ord(result[res_len - i - j - 1]) - zero_ascii
                    result[res_len - j - i - 1] = chr(s % 10 + zero_ascii)
                else:
                    result.appendleft(chr(s % 10 + zero_ascii))
    
                rem = s // 10
            if rem > 0:
                result.appendleft(chr(rem + zero_ascii))

        return "".join(result)