from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            j += 1
