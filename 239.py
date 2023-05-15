from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        queue = deque()
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.popleft()
            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        return res
