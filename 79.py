from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtracking(r, c, i, path):
            '''
            if (r, c, i) in the_cache:
                return the_cache[(r, c, i)]
            '''
            if i == len(word):
                # the_cache[(r, c, i)] = True
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in path:
                # the_cache[(r, c, i)] = False
                return False
            path.add((r, c))
            v1 = backtracking(r + 1, c, i + 1, path)
            if v1:
                return True
            v2 = backtracking(r - 1, c, i + 1, path)
            if v2:
                return True
            v3 = backtracking(r, c + 1, i + 1, path)
            if v3:
                return True
            v4 = backtracking(r, c - 1, i + 1, path)
            if v4:
                return True
            path.remove((r, c))
            return False

        for p in range(rows):
            for q in range(cols):
                the_path = set()
                if backtracking(p, q, 0, the_path):
                    return True
        return False


solve = Solution()
print(solve.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
