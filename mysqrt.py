# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        st, en, mid = 0, x, x // 2

        while st <= en:
            res = mid * mid
            if res == x:
                return mid
            
            if res > x:
                en = mid - 1
            else:
                st = mid + 1
            mid = (en + st) // 2
    
        return mid