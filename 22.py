from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(opened, closed, curStr):
            if opened == closed == n:
                res.append(curStr)
                return
            if opened < n:
                backtracking(opened + 1, closed, curStr + '(')
            if closed < opened:
                backtracking(opened, closed + 1, curStr + ')')
        backtracking(0, 0, '')
        return res


solve = Solution()
print(solve.generateParenthesis(3))
