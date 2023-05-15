from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        prev = 0
        current = 1
        while current < len(nums):
            if nums[current] == nums[prev] + 1:
                pass
            elif nums[current] == nums[prev] + 2:
                res.append(str(nums[prev]+1))
            else:
                res.append(f"{nums[prev]+1}->{nums[current]-1}")
            current += 1
            prev += 1
        return res


solve = Solution()
print(solve.findMissingRanges([0,1,3,50,75], 0, 99))

