# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subs = []
        l = len(nums)
        nums.sort()
        def solve(sub: list[int], start: int):
            if start <= l:
                subs.append(sub.copy())
            
            for i in range(start, l):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                sub.append(nums[i])
                solve(sub, i + 1)
                sub.pop()
        
        solve([], 0)
        return subs
