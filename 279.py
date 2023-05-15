class Solution:
    def numSquares(self, n: int):
        the_cache = {}

        def backtracking(value):
            if value in the_cache:
                return the_cache[value]
            if value == 0:
                return 0
            the_cache[value] = float("inf")
            k = 1
            while k*k <= value:
                the_cache[value] = min(the_cache[value], 1 + backtracking(value - k*k))
                k += 1
            return the_cache[value]
        return backtracking(n)

solve = Solution()
print(solve.numSquares(8))
