from typing import List


class Solution:
    def findPeakElement(self, nums) -> int:
        nums.insert(0, -float("inf"))
        nums.append(-float("inf"))
        l, r = 1, len(nums)-2
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m-1
            elif nums[m+1] > nums[m] > nums[m-1]:
                l = m + 1
                continue
            elif nums[m-1] > nums[m] > nums[m+1]:
                r = m - 1
                continue
            else:
                l = m + 1


solve = Solution()
print(solve.findPeakElement([1,2,3,1]))
