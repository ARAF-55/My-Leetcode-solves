class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = a ^ b
        carry = (a & b) << 1
        while carry != 0 and carry != -0:
            temp = res
            res = res ^ carry
            carry = (temp & carry) << 1
        return res


solve = Solution()
print(solve.getSum(-2, 3))