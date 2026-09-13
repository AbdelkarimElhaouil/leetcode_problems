class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        unique_len = len(unique)

        for i in range(unique_len):
            nums[i] = unique[i]
        
        return len(unique)