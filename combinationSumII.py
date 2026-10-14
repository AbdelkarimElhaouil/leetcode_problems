# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        combs = []
        candidates.sort()
        l = len(candidates)
        def solve(start: int, combo: list[int], combo_sum: int, used: list[int]):
            if combo_sum == target:
                combs.append(combo.copy())
                return
            for i in range(start, l):
                if i > 0 and candidates[i - 1] == candidates[i] and (i - 1) not in used:
                    continue
                if combo_sum + candidates[i] > target:
                    return
                combo.append(candidates[i])
                used.add(i)
                solve(i + 1, combo, combo_sum + candidates[i], used)
                combo.pop()
                used.remove(i)
        
        solve(0, [], 0, set())
        return combs
