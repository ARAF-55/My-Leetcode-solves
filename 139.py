from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        the_cache = [False]*(len(s) + 1)
        the_cache[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i-1 + len(word) < len(s) and s[i:i+len(word)] == word:
                    the_cache[i] = the_cache[i + len(word)]
                if the_cache[i]:
                    break

        return the_cache[0]


solve = Solution()
print(solve.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
