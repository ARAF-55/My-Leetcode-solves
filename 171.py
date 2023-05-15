class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = p = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            res += 26 ** p * (ord(columnTitle[i]) - ord("A") + 1)
            p += 1
        return res


solve = Solution()
print(solve.titleToNumber("ZY"))
