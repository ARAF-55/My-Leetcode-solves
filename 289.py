from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        for r in range(rows):
            for c in range(cols):
                living_count = 0
                for i, j in directions:
                    if 0 <= r + i < rows and 0 <= c + j < cols:
                        if board[r + i][c + j] == 1 or board[r + i][c + j] == '*':
                            living_count += 1
                if board[r][c] == 1:
                    if living_count < 2 or living_count > 3:
                        board[r][c] = '*'
                else:
                    if living_count == 3:
                        board[r][c] = '#'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '*':
                    board[r][c] = 0
                elif board[r][c] == '#':
                    board[r][c] = 1
        return


board = [[1,1],[1,0]]
solve = Solution()
solve.gameOfLife(board)
print(board)
