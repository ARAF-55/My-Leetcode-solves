from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def merge(l, m, r):
            n1 = m - l + 1
            n2 = r - m
            L = [0] * n1
            R = [0] * n2
            for i in range(n1):
                L[i] = nums[l + i]
            for i in range(n2):
                R[i] = nums[m + 1 + i]
            i = j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] + R[j] >= R[j] + L[i]:
                    nums[k] = L[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = R[j]
                    k += 1
                    j += 1

            while i < n1:
                nums[k] = L[i]
                k += 1
                i += 1

            while j < n2:
                nums[k] = R[j]
                k += 1
                j += 1

        def mergeSort(l, r):
            if l < r:
                m = (l + r) // 2
                mergeSort(l, m)
                mergeSort(m + 1, r)
                merge(l, m, r)
            return nums

        nums = mergeSort(0, len(nums) - 1)
        return str(int("".join(nums)))


solve = Solution()
print(solve.largestNumber([3, 30, 34, 5, 9]))
