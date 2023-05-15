class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        divided_by_5 = n // 5
        return divided_by_5 + self.trailingZeroes(n // 5)


solve = Solution()
print(solve.trailingZeroes(0))
