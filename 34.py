from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        i = [-1, -1]

        def search(l, r, left_bias):
            if l > r:
                return
            while l <= r:
                m = (l + r) // 2
                if target == nums[m]:
                    if left_bias:
                        i[0] = m
                        search(l, m - 1, True)
                        break
                    else:
                        i[1] = m
                        search(m + 1, r, False)
                        break
                elif target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1

        search(l, r, True)
        search(l, r, False)
        return i


solve = Solution()
value = solve.searchRange([5, 7, 7, 8, 8, 10], 100)
print(value)
