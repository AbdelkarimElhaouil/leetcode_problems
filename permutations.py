# 46. Permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = []
        l = len(nums)
        def backtrack(perm: list[int]) -> None:
            if l == len(perm):
                perms.append(perm.copy())
                return
    
            for i in range(l):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack(perm)
                perm.pop()
        
        backtrack([])
        return perms
