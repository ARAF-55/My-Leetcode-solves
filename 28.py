class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) <= len(needle):
            if haystack == needle:
                return 0
            return -1
        k = len(haystack) - len(needle)
        for i in range(0, k + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


solve = Solution()
print(solve.strStr("abc", ""))
