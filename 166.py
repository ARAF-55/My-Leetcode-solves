class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator < 0 < denominator:
            sign = "-"
        elif denominator < 0 < numerator:
            sign = "-"
        else:
            sign = ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = sign + str(numerator // denominator)
        if numerator % denominator:
            res += '.'
            remainder = numerator % denominator
            the_map = {remainder: len(res)}
            i = len(res)
            while remainder:
                remainder *= 10
                res += str(remainder // denominator)
                remainder = remainder % denominator
                if remainder in the_map:
                    return res[:the_map[remainder]] + '(' + res[the_map[remainder]:i + 1] + ')'
                i += 1
                the_map[remainder] = i
            return res
        else:
            return res


solve = Solution()
print(solve.fractionToDecimal(4, -333))
