global res_r, res_l


class Solution:
    def longestPalindrome(self, s: str) -> str:
        global res_l, res_r
        result_length = 0
        n = 0
        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > result_length:
                    res_l = L
                    res_r = R
                    result_length = R - L + 1
                    n += 1
                L -= 1
                R += 1
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > result_length:
                    res_l = L
                    res_r = R
                    result_length = R - L + 1
                    n += 1
                L -= 1
                R += 1
        if n != 0:
            return s[res_l: res_r + 1]
        else:
            return ''


solve = Solution()
res = solve.longestPalindrome("cbbd")
print(res)
