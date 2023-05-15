from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[j] > prices[i]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return profit


solve = Solution()
print(solve.maxProfit([7,6,4,3,1]))