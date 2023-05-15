import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        else:
            if n < 0:
                n *= -1
            if n % 2:
                first_part = self.myPow(x, n // 2)
                return first_part * first_part * x
            else:
                first_part = self.myPow(x, n // 2)
                return first_part * first_part


solve = Solution()
val = solve.myPow(2, -2)
print(val)
