import math


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        last_valid = 7 if x >= 0 else -8
        Max = 2147483647
        Min = -2147483648
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if result > Max//10 or (result == Max//10 and digit > last_valid):
                return 0
            if result < int(Min/10) or (result == int(Min/10) and digit < last_valid):
                return 0
            result = result * 10 + digit
        return result



solve = Solution()
value = solve.reverse(1463847412)
print(value)
