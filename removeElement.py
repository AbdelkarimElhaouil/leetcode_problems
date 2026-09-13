# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        start = 0
        while start <= last:
            if nums[last] == val:
                last -= 1
            elif nums[start] != val:
                start += 1
            else:
                tmp = nums[last]
                nums[last] = nums[start]
                nums[start] = tmp
                start += 1
                last -= 1
        return start