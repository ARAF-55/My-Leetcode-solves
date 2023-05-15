class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p = ''
        l = 0
        while l < len(s):
            if ord(s[l]) in range(97, 123) or ord(s[l]) in range(48, 58):
                p += s[l]
            l += 1
        print(p)
        if p == p[::-1]:
            return True
        else:
            return False


solve = Solution()
print(solve.isPalindrome("A man, a plan, a canal: Panama"))
