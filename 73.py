from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        row1 = False
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    if r > 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
                    else:
                        row1 = True
                        matrix[0][c] = 0
        for c in range(1, columns):
            for r in range(1, rows):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if row1:
            for c in range(columns):
                matrix[0][c] = 0


solve = Solution()
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solve.setZeroes(matrix)
print(matrix)
