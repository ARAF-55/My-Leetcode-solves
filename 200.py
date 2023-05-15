from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == '0':
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                the_val = queue.popleft()
                p, q = the_val
                if p + 1 < rows and grid[p+1][q] == '1' and (p + 1, q) not in visited:
                    queue.append((p + 1, q))
                    visited.add((p + 1, q))
                if p - 1 >= 0 and grid[p-1][q] == '1' and (p - 1, q) not in visited:
                    queue.append((p - 1, q))
                    visited.add((p - 1, q))
                if q + 1 < cols and grid[p][q+1] == '1' and (p, q+1) not in visited:
                    queue.append((p, q + 1))
                    visited.add((p, q + 1))
                if q - 1 >= 0 and grid[p][q-1] == '1' and (p, q-1) not in visited:
                    queue.append((p, q - 1))
                    visited.add((p, q-1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    bfs(r, c)
        return res


solve = Solution()
print(solve.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
