class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        l = len(nums)
        def backtrack(subset: list[int], start_ind: int):
            if subset not in res:
                res.append(subset.copy())

            for i in range(start_ind, l):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        backtrack([], 0)
        return res
    
s = Solution()

print(s.subsets([1, 2, 3]))