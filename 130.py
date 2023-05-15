from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if (i, j) in self.visited:
                return
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            self.visited.add((i, j))
            board[i][j] = "T"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        dfs(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
        return






