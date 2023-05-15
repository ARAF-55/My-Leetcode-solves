from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bottom = 0, len(matrix) - 1
        while top < bottom:
            l, r = top, bottom
            i = 0
            while i < r - l:
                var = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = var
                i += 1
            top += 1
            bottom -= 1


matrixis = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solve = Solution()
solve.rotate(matrixis)
print(matrixis)
