class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            elif j >= len(p):
                return False
            matched = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = dfs(i, j + 2) or (matched and dfs(i + 1, j))
                return cache[(i, j)]
            if matched:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        res = dfs(0, 0)
        return res


solve = Solution()
val = solve.isMatch("ab", ".*")
print(val)
