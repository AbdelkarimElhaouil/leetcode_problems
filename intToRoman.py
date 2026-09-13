# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        m = int(num / 1000)
        if m != 0:
            res = m * 'M'
            num = num % 1000
        print(res)
        m = int(num / 900)
        if m != 0:
            res = res + 'CM'
            num = num % 900
        m = int(num / 500)
        if m != 0:
            res = res + 'D'
            num = num % 500
        m = int(num / 400)
        if m != 0:
            res = res + m * 'CD'
            num = num % 400
        print(res)
        m = int(num / 100)
        if m != 0:
            res = res + m * 'C'
            num = num % 100
        m = int(num / 90)
        if m != 0:
            res = res + 'XC'
            num = num % 90
        m = int(num / 50)
        if m != 0:
            res = res + 'L'
            num = num % 50
        m = int(num / 40)
        if m != 0:
            res = res + m * 'XL'
            num = num % 40
        m = int(num / 10)
        if m != 0:
            res = res + m * 'X'
            num = num % 10
        m = int(num / 9)
        if m != 0:
            res = res + 'IX'
            num = num % 9
        m = int(num / 5)
        if m != 0:
            res = res + 'V'
            num = num % 5
        m = int(num / 4)
        if m != 0:
            res = res + m * 'IV'
            num = num % 4
        m = int(num / 1)
        if m != 0:
            res = res + m * 'I'
            num = num % 1
        return res