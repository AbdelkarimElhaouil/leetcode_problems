# 3550. Smallest Index With Digit Sum Equal to Index

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = 0
            while nums[i]:
                s += nums[i] % 10
                nums[i] //= 10
            if s == i:
                return i

        return -1