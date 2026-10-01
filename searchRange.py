# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = -1
        right = -1
        l = len(nums)
        st, end, mid = 0, l - 1, l // 2

        if not nums:
            return [-1, -1]

        while st <= end:
            if nums[mid] == target:
                left = mid
                end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                st = mid + 1
            mid = (st + end) // 2
        
        st, end, mid = 0, l - 1, l // 2

        while st <= end:
            if nums[mid] == target:
                    right = mid
                    st = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                st = mid + 1
            mid = (st + end) // 2

        return [left, right]


