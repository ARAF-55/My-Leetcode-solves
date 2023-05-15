from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        result = 0
        while L < R:
            if height[L] > height[R]:
                val = height[R] * (R - L)
                R -= 1
                if val > result:
                    result = val
            else:
                val = height[L] * (R - L)
                L += 1
                if val > result:
                    result = val
        return result


solve = Solution()
res = solve.maxArea([1,1])
print(res)
