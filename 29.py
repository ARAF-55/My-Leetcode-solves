class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div = abs(dividend)
        divs = abs(divisor)
        result = 0
        while div >= divs:
            decrement = divs
            counter = 1
            while div >= decrement:
                div -= decrement
                result += counter
                decrement += decrement
                counter += counter

        if dividend < 0 < divisor or divisor < 0 < dividend:
            return max(-result, -2147483648)
        else:
            return min(result, 2147483647)


solve = Solution()
print(solve.divide(10, 3))
