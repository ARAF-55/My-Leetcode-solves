from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        stack = ''

        def backtracking(i, stack_val=None):
            if len(digits) == len(stack_val):
                res.append(stack_val)
                return
            for c in h_map[digits[i]]:
                stack_val += c
                backtracking(i + 1, stack_val)
                stack_val = stack_val[0: len(stack_val) - 1]
            return

        if digits:
            backtracking(0, stack)
        return res


solve = Solution()
result = solve.letterCombinations("23")
print(result)
