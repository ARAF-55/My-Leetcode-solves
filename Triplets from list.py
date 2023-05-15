from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        z = []
        p = []
        n = []
        r = set()
        for i in nums:
            if i < 0:
                n.append(i)
            elif i > 0:
                p.append(i)
            else:
                z.append(i)
        N, P = set(n), set(p)
        if z:
            for i in P:
                if -1 * i in N:
                    r.add((-1 * i, 0, i))
        if len(z) > 2:
            r.add((0, 0, 0))
        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    r.add(tuple(sorted([p[i], p[j], target])))
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    r.add(tuple(sorted([n[i], n[j], target])))
        return r


solve = Solution()
val = solve.threeSum([-1,0,1,2,-1,-4])
print(val)