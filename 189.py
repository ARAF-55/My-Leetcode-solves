from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[-(len(nums)-k)-1::-1]
        nums[k:] = nums[:-(len(nums)-k)-1:-1]


nums = [1, 2, 3, 4, 5, 6, 7]
solve = Solution()
solve.rotate(nums, k=3)
print(nums)
