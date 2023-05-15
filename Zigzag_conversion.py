class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        if numRows == 1:
            return s
        else:
            for i in range(numRows):
                if i == 0:
                    val = 0
                    while val < len(s):
                        res += s[val]
                        val += (numRows - 1) * 2
                elif i == (numRows - 1):
                    val = numRows - 1
                    while val < len(s):
                        res += s[val]
                        val += (numRows - 1) * 2
                else:
                    mid = i
                    lola = 0
                    while mid < len(s):
                        res += s[mid]
                        if lola % 2 == 0:
                            mid += (numRows - 1) * 2 - 2 * i
                            lola += 1
                        else:
                            mid += 2 * i
                            lola += 1
            return res


solve = Solution()
value = solve.convert("A", 1)
print(value)
