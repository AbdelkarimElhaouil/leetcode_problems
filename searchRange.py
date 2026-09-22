# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        st, end, mid = 0, l, l // 2

        while st <= end:
            if target == nums[mid]:
                if mid > 0 and nums[mid - 1] == target:
                    return [mid - 1, mid]
                if mid < l - 1 and nums[mid + 1] == target:
                    return [mid, mid + 1] 
                return [mid, mid]
            elif target > nums[mid]:
                st = mid + 1
                mid = (st + end) // 2
            else:
                end = mid - 1
                mid = (st + end) // 2

        return [-1, -1]


s = Solution()

nums = [1, 1, 1, 1]

print(s.searchRange(nums, 1))