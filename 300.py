from typing import List


class Solution:
    def __init__(self):
        self.max = 0
    def lengthOfLIS(self, nums: List[int]) -> int:
        the_cache = {}

        def backtracking(i):
            if i in the_cache:
                return the_cache[i]
            if i == len(nums):
                return 0
            value = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    value = max(value, 1 + backtracking(j))
            the_cache[i] = value
            self.max = max(self.max, value)
            return value

        for k in range(len(nums)):
            if k not in the_cache:
                backtracking(k)
        return self.max




solve = Solution()
print(solve.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
