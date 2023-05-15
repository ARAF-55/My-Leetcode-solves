from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        largest = 0
        stack = []
        for index, height in enumerate(heights):
            begin = index
            while stack and stack[-1][1] > height:
                idx, value = stack.pop()
                largest = max(largest, value * (index - idx))
                begin = idx
            stack.append((begin, height))
        return largest


solve = Solution()
print(solve.largestRectangleArea([]))
