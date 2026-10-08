class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        l = len(candidates)
        def solve(nums: list[int], comb: list[int], comb_sum: int):
            if comb_sum == target:
                res.append(comb.copy())
                return
            elif comb_sum > target:
                return
            
            for i in range(l):
                if res and any(nums[i] == r[0] for r in res):
                    continue
                comb.append(nums[i])
                solve(nums, comb, comb_sum + nums[i])
                comb.pop()
        solve(candidates, [], 0)
        return res