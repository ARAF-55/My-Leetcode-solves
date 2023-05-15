from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(low, high):
            i, j = low - 1, low
            while j < high:
                if nums[j] <= nums[high]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quickSort(l, r):
            if l < r:
                index = partition(l, r)
                if index == len(nums) - k:
                    return nums[index]
                elif index < len(nums) - k:
                    return quickSort(index + 1, r)
                else:
                    return quickSort(l, index - 1)
            return nums[l]

        return quickSort(0, len(nums) - 1)


solve = Solution()
print(solve.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
