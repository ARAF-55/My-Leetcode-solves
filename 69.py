class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            p = mid * mid
            if p == x:
                return mid
            elif p > x:
                r = mid - 1
            else:
                l = mid + 1
        return r


solve = Solution()
print(solve.mySqrt(25))
