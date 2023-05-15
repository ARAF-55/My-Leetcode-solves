from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        starter = intervals[0][0]
        ender = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ender:
                ender = max(ender, intervals[i][1])
            else:
                res.append([starter, ender])
                starter = intervals[i][0]
                ender = intervals[i][1]
        res.append([starter, ender])
        return res


solve = Solution()
print(solve.merge([[1, 4]]))
