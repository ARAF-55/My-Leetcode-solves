from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            val = []
            for j in range(i+1):
                if j == i or j == 0:
                    val.append(1)
                else:
                    node = res[-1]
                    val.append(node[j]+node[j-1])
            res.append(val.copy())
        return res


solve = Solution()
print(solve.generate(4))


