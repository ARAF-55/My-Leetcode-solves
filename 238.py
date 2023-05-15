from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        val = 1
        for i in range(len(nums)):
            res[i] = val
            val *= nums[i]
        val = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= val
            val *= nums[j]
        return res


solve = Solution()
print(solve.productExceptSelf([1, 2, 3, 4]))
