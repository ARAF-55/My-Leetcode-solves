from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maximum = 1
        for i in range(len(points) - 1):
            x1, y1 = points[i][0], points[i][1]
            the_cache = {}
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2:
                    m = "vertical"
                else:
                    m = (y1 - y2) / (x1 - x2)
                the_cache[m] = 1 + the_cache.get(m, 1)
                maximum = max(maximum, the_cache[m])
        return maximum


solve = Solution()
print(solve.maxPoints([[1,1]]))
