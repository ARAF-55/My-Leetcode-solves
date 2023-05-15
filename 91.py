class Solution:
    def numDecodings(self, s: str) -> int:
        the_cache = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0':
                op1 = the_cache[i + 1]
            else:
                op1 = 0
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                op2 = the_cache[i + 2]
            else:
                op2 = 0
            the_cache[i] = op1 + op2
        return the_cache[0]


solve = Solution()
print(solve.numDecodings("226"))
