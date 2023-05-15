from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, k = 0, 1, 2
        profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = profit + prices[j] - prices[i]
            i += 1
            j += 1
        return profit


solve = Solution()
print(solve.maxProfit([7]))
