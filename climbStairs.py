# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        mem = (n + 1) * [-1]
        def dp(x: int):
            if mem[x] != -1:
                return mem[x]
            elif x <= 2:
                mem[x] = x
            else:
                mem[x] = dp(x - 1) + dp(x - 2)
            return mem[x]
    
        return dp(n)