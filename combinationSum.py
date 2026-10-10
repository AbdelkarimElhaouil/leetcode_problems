# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        l = len(candidates)
        candidates.sort()
        def solve(start: int, comb: list[int], comb_sum: int):            
            if comb_sum == target:
                res.append(comb.copy())
                return

            for i in range(start, l):
                if comb_sum + candidates[i] > target:
                    return
                
                comb.append(candidates[i])
                solve(i, comb, comb_sum + candidates[i])
                comb.pop()
        
        solve(0, [], 0)
        return res