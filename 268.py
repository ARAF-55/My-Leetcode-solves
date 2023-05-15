from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        value = int(n * (n+1)/2)
        for i in nums:
            value -= i
        return value
