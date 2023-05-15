from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def get_one_valid_partition(length):
            if length == len(s):
                res.append(stack.copy())
                return
            for i in range(length, len(s)):
                if self.check_palindrome(s[length:i + 1]):
                    stack.append(s[length:i + 1])
                    get_one_valid_partition(i + 1)
                    stack.pop()
            return

        get_one_valid_partition(0)
        return res

    def check_palindrome(self, the_string):
        if the_string == the_string[::-1]:
            return True
        else:
            return False


solve = Solution()
print(solve.partition("aab"))
