from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(enumerate(nums))
        res = [0] * len(nums)

        def merge(l, m, r):
            n1 = m - l + 1
            n2 = r - m
            L = nums[l:m+1]
            R = nums[m+1:r+1]
            i, j, k = 0, 0, l

            while i < n1 and j < n2:
                if L[i][1] <= R[j][1]:
                    nums[k] = L[i]
                    res[L[i][0]] += j
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = L[i]
                res[L[i][0]] += j
                i += 1
                k += 1

            while j < n2:
                nums[k] = R[j]
                j += 1
                k += 1
            return

        def mergeSort(l, r):
            if l < r:
                m = (l + r) // 2
                mergeSort(l, m)
                mergeSort(m+1, r)
                merge(l, m, r)
            return

        mergeSort(0, len(nums)-1)
        return res



solve = Solution()
print(solve.countSmaller([5, 2, 6, 1]))
