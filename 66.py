from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = 0
        multiplier = 1
        res = []
        for i in range(len(digits) - 1, -1, -1):
            value += digits[i] * multiplier
            multiplier *= 10
        value += 1
        multiplier = 10
        while value > 0:
            res.insert(0, value % multiplier)
            value = int(value // multiplier)
        return res


solve = Solution()
print(solve.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))
