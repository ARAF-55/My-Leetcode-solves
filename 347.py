from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        the_map = {}
        res = []

        for i in nums:
            the_map[i] = 1 + the_map.get(i, 0)

        val = []
        for j in range(len(nums)):
            val.append([])
        for num, times in the_map.items():
            val[times - 1].append(num)
        for i in range(len(val) - 1, -1, -1):
            for j in val[i]:
                res.append(j)
                if len(res) == k:
                    return res


solve = Solution()
print(solve.topKFrequent(nums =
[3,0,1,0],
k =
1))