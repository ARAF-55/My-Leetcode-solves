from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        the_set = set(nums)
        result = 0
        for i in nums:
            if i-1 not in the_set:
                sequence_length = 1
                while i+sequence_length in the_set:
                    sequence_length += 1
                result = max(result, sequence_length)

        return result


solve = Solution()
print(solve.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))





