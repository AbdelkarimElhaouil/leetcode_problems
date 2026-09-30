# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = len(nums)
        st, en, mid = 0, l - 1, l // 2

        while st <= en:
            if nums[mid] == target:
                return mid
            
            elif nums[st] <= nums[mid]:
                if nums[mid] >= target >= nums[st]:
                    en = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[en] >= target >= nums[mid]:
                    st = mid + 1
                else:
                    en = mid - 1
            mid = (st + en) // 2
        return -1
            
