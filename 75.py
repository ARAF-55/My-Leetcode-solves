from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        j = 0
        i = -1
        k = len(nums)

        def swap(h, m):
            temp = nums[h]
            nums[h] = nums[m]
            nums[m] = temp

        while j < k:
            if nums[j] < 1:
                i += 1
                swap(i, j)
                j += 1
            elif nums[j] > 1:
                k -= 1
                swap(j, k)
            else:
                j += 1


solve = Solution()
nums_set = [2, 2, 2, 2]
solve.sortColors(nums_set)
print(nums_set)
