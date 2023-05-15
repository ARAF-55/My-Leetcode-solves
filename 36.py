from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_vals = defaultdict(set)
        column_vals = defaultdict(set)
        portion_vals = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_vals[i]:
                    return False
                else:
                    row_vals[i].add(board[i][j])
                if board[i][j] in column_vals[j]:
                    return False
                else:
                    column_vals[j].add(board[i][j])
                row = i // 3
                col = j // 3
                if board[i][j] in portion_vals[(row, col)]:
                    return False
                else:
                    portion_vals[(row, col)].add(board[i][j])
        return True

