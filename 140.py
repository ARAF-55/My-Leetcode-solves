from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        stack = []

        def backtracking(index):
            if index == len(s):
                res.append(" ".join(stack))
                return
            for i in range(index, len(s)):
                if s[index: i+1] in wordDict:
                    stack.append(s[index: i+1])
                    backtracking(i+1)
                    stack.pop()

        backtracking(0)
        return res
