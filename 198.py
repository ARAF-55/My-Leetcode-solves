from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(i):
            if i >= len(nums):
                return 0
            op1 = nums[i] + robbing(i + 2)
            op2 = robbing(i + 1)
            return max(op1, op2)

        return robbing(0)
