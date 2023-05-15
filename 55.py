from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        while i != 0:
            stepper = 0
            for j in range(i - 1, -1, -1):
                if nums[j] >= (i - j):
                    stepper = 1
                    break
                else:
                    continue
            if stepper == 1:
                i = j
                continue
            else:
                return False
        return True


solve = Solution()
print(solve.canJump([3]))
