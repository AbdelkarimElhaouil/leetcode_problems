# 75. Sort Colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        end, st, mid = len(nums) - 1, 0, 0
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[st] = nums[st], nums[mid]
                mid += 1
                st += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1