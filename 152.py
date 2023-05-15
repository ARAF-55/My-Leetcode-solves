from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_val = 1
        min_val = 1
        for i in nums:
            temp_val = max_val
            max_val = max(max_val*i, min_val*i, i)
            min_val = min(temp_val*i, min_val*i, i)
            res = max(res, max_val)
        return res

