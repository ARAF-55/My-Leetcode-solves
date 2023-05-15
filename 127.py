from typing import List
from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.result = 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        the_edges = defaultdict(list)
        wordList.append(beginWord)
        for c in wordList:
            for i in range(len(c)):
                the_pattern = c[:i] + '*' + c[i+1:]
                the_edges[the_pattern].append(c)

        def bfs():
            visited = set()
            visited.add(beginWord)
            queue = deque()
            queue.append(beginWord)
            while queue:
                the_size = len(queue)
                for _ in range(the_size):
                    present_word = queue.popleft()
                    if present_word == endWord:
                        return self.result
                    for x in range(len(present_word)):
                        pattern = present_word[:x] + '*' + present_word[x + 1:]
                        for values in the_edges[pattern]:
                            if values not in visited:
                                visited.add(values)
                                queue.append(values)
                self.result += 1
            return 0
        return bfs()


solve = Solution()
print(solve.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
