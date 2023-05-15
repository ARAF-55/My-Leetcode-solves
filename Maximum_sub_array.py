from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_value = nums[0]
        total_value = 0
        for i in nums:
            total_value += i
            maximum_value = max(maximum_value, total_value)
            if total_value < 0:
                total_value = 0
        return maximum_value


solve = Solution()
value = solve.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(value)
