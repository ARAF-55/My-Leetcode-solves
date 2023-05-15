from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        l, r = 0, len(matrix[0])
        res = []
        while l < r and top < bottom:
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            if top == bottom:
                break
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1
            if l == r:
                break
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            if top == bottom:
                break
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l == r:
                break
        return res


solve = Solution()
result = solve.spiralOrder([[6, 7, 9]])
print(result)
