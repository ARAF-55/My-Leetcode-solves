from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start_points = [(L, -H, R) for L, R, H in buildings]
        end_points = [(R, 0, "don't need") for L, R, H in buildings]
        all_points = start_points + end_points
        all_points.sort()
        result = [(0, 0)]
        min_heap = [(0, float("Inf"))]

        for x, y, x2 in all_points:
            while x >= min_heap[0][1]:
                heapq.heappop(min_heap)
            if y:
                heapq.heappush(min_heap, (y, x2))
            curMax = -min_heap[0][0]
            if result[-1][1] != curMax:
                result.append([x, curMax])
        return result[1:]



