# 47. Permutations II

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        permutations = []
        l = len(nums)
        nums.sort()
        def solve(perm: list[int], used_ind: list[int]) -> None:
            if len(perm) == l:
                permutations.append(perm.copy())
                return
            for i in range(l):
                if i in used_ind:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in used_ind:
                    continue
                used_ind.append(i)
                perm.append(nums[i])
                solve(perm, used_ind)
                perm.pop()
                used_ind.pop()
        solve([], [])
        return permutations
        
                